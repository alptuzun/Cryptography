# use "pip install sympy" if sympy is not installed
import random
import sympy
import warnings

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    if a < 0:
        a = a+m
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    
def random_prime(bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        p = random.randrange(2**(bitsize-1), 2**bitsize-1)
        chck = sympy.isprime(p)
    warnings.simplefilter('default')    
    return p

def large_DL_Prime(q, bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        k = random.randrange(2**(bitsize-1), 2**bitsize-1)
        p = k*q+1
        chck = sympy.isprime(p)
    warnings.simplefilter('default')    
    return p

def Param_Generator(qsize, psize):
    q = random_prime(qsize)
    p = large_DL_Prime(q, psize-qsize)
    tmp = (p-1)//q
    g = 1
    while g == 1:
        alpha = random.randrange(1, p)
        g = pow(alpha, tmp, p)
    return q, p, g

# Generating private-public key pair
def Key_Gen(q, p, g):
    s = random.randint(1, q) # private key
    h = pow(g, s, p)         # public key
    return s, h

# Encryption
def Enc(message, h, q, p, g): # m is the message
    m = int.from_bytes(message, byteorder='big')
    k = random.randint(1, 2**16-1)
    r = pow(g, k, p)
    t = (pow(h, k, p)*m)%p
    return r, t

# Decryption
def Dec(r, t, s, q, p, g):
    m = (pow(r, q-s, p)*t)%p
    return m.to_bytes((m.bit_length()+7)//8, byteorder='big')

q1 = 15149502636477230313708825444958172381062420832611909277967694924141
p1 = 17171810507527611827459888970482558280049759629590793472150559723765848711383835049245937646549939397966259641645103225531930421645608431243042298893897244466652614451421686619053210900424772468013950224816517952238385741132939187922452018984703453411288012329886491758408994179274945133094525718704344872516320174036615158401163102965189811705576881636295731669371188837567695068724031496729629325939591544188700658762744573621881013382784812327126130889653994619368746615568643385510999994642583561480234818951554659200389561319173722050520900128018410903049915827147459638060630603549232119713008292573437433453497
g1 = 16504112626086834307562556557911516801482436189796980917569437678802258423627806531088880182798603958135934374454215115464224501620226427479253834359335927567103141261111369756955806052590791482920380442557084258376180722805195110785020712662517021636062482848271665130841421286183178099472793402104717610977214679807491857436937503954660977499933007331215434060397046183381499506296987451038706150929750626015618873704604170729141396104894631584189750219098304416594911696564839857836438110241542476458957516019484803515042648963320942369364126124313576091775543052858003081488799215856920266461135624985038068743185
h = 13373848373727304074099573872186124895161117024560803703177901487562787289757370845910389854469546958123597643116457701586143804625723945169095161154692314666702832132479134348883985791840884424822847882737601768024240458862780435495409688087238094497578702448753271801960397686889078516347068330894832234577133949588283577126698411529224980198563628407117724224985340210273029021686218616427626236030718399898318567447998321086723611910772215661146185899194156398634787110176501068954426328714562457060259031521608426942771568667701832844365311770664034884391530680217866060773799463247572987374602413392645452613640
r = 14580602664294001274034633676919139107987868328875858365210024793254972717270097373518264956814973589933955155463165461411853831030877016076206131973924043144201347158167805837391932969457772052471526069681686350096199327827009059266143203785755949549436355719627786929114313049732640144567103119627180304101971994665090794489890193574241345628502628652199408779233388816942828648434257460644626506323604151334383753506018126066682418102617777994406459003384865107538075587771611036550416944875543450064240089041596421259607748082976461301064066032475153360385068064863314804124679983423871349361671859752839124503218
t = 2197972781178017162448087755096864423893281135511366947383233515019552485487819668953931225593097251025109297577662745346022041290548338865519391240280077428989987283539048731688312589885841222996426195917602190629041975255270391054887169826613827629997131792031249257443219336078567657442198939766798664067508917665443260370491499590584900913900071729679396892277016877923649319632123379734565631286496085104823047980924930299126319159284697409608679671176571989977647906559552435039733460762948852653149229376885570373881284278928955770440410461633709314225496884902626988287771853109576076808689758788807918785694

# implementation flaw in this ElGamal algorithm is that the randomly generated k in Encryption is in the range between (1,2^16-1) not in the range of (1, q-1).
# This results in an incredible reduction in the size of all possible random values that k can take so the finding the values are significantly easier
k = None
print(modinv(h, p1))
# try for all possible random k values
for i in range(1, 2**16 - 1):
    if (pow(g1, i, p1) == r):
        k = i
        print("The random value k is: ", k)
        break
# t = h^k * m mod p, m = t * (h^k)^-1 mod p
m1 = (t * modinv(pow(h, k), p1)) % p1
# decode the binary string m to a plaintext
plaintext = m1.to_bytes((m1.bit_length() // 8 + 1), byteorder="big").decode()
# The hidden message is: It begins, as most things begin, with a song. 
print("The hidden message is: ", plaintext)

# second part, namely question 4

# Let's set the required parameters
q2 = 1267563829357910721192610532349240957905695824701
p2 = 154474724567024505552326668667624254530346668891516550168600112845390987269072109602304547293643022259327026218001120791870575104603071951983783939178506546068762532687120696273925570767784225223472959435756693935028851519062765262076784037127804385249530791458749773813851085918817576722179601544649985814629
g2 = 103909996904124632993131371858766165669729607982465958461739488117164223912656915892337662801494883198703452648194921406170215661998544589380930634851778368778250267832833231632014974502522850108470857947473599059781490699897828182798112413851433613933100792383641135076229528835761463113619032894070860192807
message1 = b'This is my last message to you'
r1 = 138463133012013282634913641892758158801762848592172407698472135927781184457014021159308423563284158903125454277831143312262376170389801812594838453962655356699229091103625269373494506043148105103719155747470849279981239429070325302155209235130687521331639091969580507394146320441457615197051837733672345300228
t1 = 106265595589369404671099487302170469354962925840925742209713793365234534431026758828912055935037813410518539768824133366973085636520219854456990152125504837648179032393648480733938344778228349463627323405812952123710763683733706558368525987706254967419548469786325235631013665472833542539156237682564045597699
r2 = 138463133012013282634913641892758158801762848592172407698472135927781184457014021159308423563284158903125454277831143312262376170389801812594838453962655356699229091103625269373494506043148105103719155747470849279981239429070325302155209235130687521331639091969580507394146320441457615197051837733672345300228
t2 = 135563059487582975121566088062898494475175255003560071628710046462630442262636134689239784950989051760061880686659805280094257722717904505303535034697677080651092788318486681967488775262340037022020363930212423666424280959617684767562766700269012486352837430312759302045630777452835207236487134484258912710865
# Here it can be easily seen that the r1 and r2 are equal and that implies that the random k values are also same sine r = g^k mod p
# Additionally, because the k values are same, h^k values are also same and with that we can use the t = h^k * m mod p to derive the message
# Before starting, we need to convert the binary string to a integer sequence
message1_int = int.from_bytes(message1, "big")
h_k = (t1 * modinv(message1_int, p2)) % p2
# With that information, t2 = h^k * m2 mod p and m2 = t2* (h^k)^-1 mod p 
message2_int = (t2 * modinv(h_k, p2)) % p2
# Decode the second message
message2 = message2_int.to_bytes((message2_int.bit_length() // 8 + 1), byteorder="big").decode()
# The hidden second message is:  In sorrow, seek happiness.
print("The hidden second message is: ", message2)