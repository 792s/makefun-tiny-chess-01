import json,os,urllib.request as u
V=[100,320,330,500,900,20000]
NK=(-21,-19,-12,-8,8,12,19,21)
QK=(-11,-9,9,11,-10,-1,1,10)
DG=QK[:4]
OG=QK[4:]
DS={'N':NK,'B':DG,'R':OG,'Q':QK,'K':QK}
PS=['PPPPUZZ<UKFPPPPdUUZiZZdn~~~~PPPP','!(22(<PU2UZ_2P_d2U_d2PZ_(<PP!(22','<FFFFUPPFZZZFPZZFUUZFPUZFPPP<FFF','PPPUKPPPKPPPKPPPKPPPKPPPUZZZPPPP','P'*32,'dnZPddPPF<<<<22(2((!2((!2((!2((!']
P=[[ord(s[(i//8)*4+min(i%8,7-i%8)])-80 for i in range(64)] for s in PS]
CK={98:14,91:13,28:11,21:7}
RV=lambda c:(c&1)*8+(c&2)*2+(c&4)//2+(c&8)//8
S=lambda s,x,ch:s[:x]+ch+s[x+1:]
Z='PNBRQKpnbrqk'
K=[0]*64
H={}
def F(f):
 global b,c,e,RT
 b=list(' '*20+' ........ '*8+' '*20)
 p=f.split()
 q=21
 for ch in p[0]:
  if ch=='/':q+=2
  elif ch.isdigit():q+=int(ch)
  else:b[q]=ch;q+=1
 b=''.join(b)
 c=0
 for ch,n in zip('KQkq',(1,2,4,8)):c|=n*(ch in p[2])
 e=-1 if p[3]=='-' else(10-int(p[3][1]))*10+ord(p[3][0])-96
 RT=p[1]=='b'
 if RT:
  b=b[::-1].swapcase()
  c=RV(c)
  e=119-e if e!=-1 else -1
 H[b]=H.get(b,0)+1
def A(j):
 for ds,pc in((NK,'n'),(QK,'k'),((-11,-9),'p')):
  for d in ds:
   if b[j+d]==pc:return 1
 for ds,pc in((DG,'b'),(OG,'r')):
  for d in ds:
   k=j+d
   while b[k]!=' ':
    if b[k]==pc or b[k]=='q':return 1
    if b[k]!='.':break
    k+=d
 return 0
def G(cp):
 m=[]
 for i,p in enumerate(b):
  if not p.isupper():continue
  if p=='P':
   cd=[]
   if not cp:
    j=i-10
    if b[j]=='.':
     cd+=[j]
     if i//10==8 and b[i-20]=='.':m+=[i*128+i-20]
   for d in(-11,-9):
    j=i+d
    if b[j].islower():cd+=[j]
    elif j==e:m+=[i*128+j]
   for j in cd:
    if j<30:
     for z in'QRBN':m+=[i*128+j+ord(z)*16384]
    else:m+=[i*128+j]
  else:
   for d in DS[p]:
    j=i+d
    while 1:
     q=b[j]
     if q==' ' or q.isupper():break
     if q!='.' or not cp:m+=[i*128+j]
     if p in 'NK' or q!='.':break
     j+=d
   if p=='K' and not cp:
    for kt,bt in((i+2,1),(i-2,2)):
     rf=98 if kt>i else 91
     if c&bt and b[rf]=='R' and b[min(i,rf)+1:max(i,rf)] in('..','...') and all(not A(x) for x in(i,(i+kt)//2,kt)):m+=[i*128+kt]
 return m
def M(m):
 global b,c,e
 i,j,pr=(m>>7)&127,m&127,m>>14
 o=(b,c,e)
 p=b[i]
 n=S(b,i,'.')
 n=S(n,j,chr(pr) if pr else p)
 if p=='P' and j==e:n=S(n,j+10,'.')
 if p=='K' and abs(j-i)==2:
  rf,rt=(98,j-1) if j>i else(91,j+1)
  n=S(S(n,rt,'R'),rf,'.')
 b=n
 if A(b.index('K')):
  b,c,e=o
  return 0
 k=c&CK.get(i,15)&CK.get(j,15)
 if p=='K':k&=12
 f=(i+j)//2 if p=='P' and abs(j-i)==20 else -1
 b=b[::-1].swapcase()
 c=RV(k)
 e=119-f if f!=-1 else -1
 return o
def E():
 r=0
 for j,p in enumerate(b):
  if p<'A':continue
  t=Z.index(p)%6
  i=71-j//10*8+j%10
  if p>'Z':i^=56
  x=V[t]+P[t][i]
  r+=x if p<'a' else -x
 return r
def O(ms,pl):
 def sc(m):
  if m>>14:return 9500
  q=b[m&127]
  return 10000+V[Z.index(q)%6]*10-V[Z.index(b[(m>>7)&127])%6]//10 if q!='.' else 9000 if m==K[pl] else 0
 return sorted(ms,key=sc,reverse=True)
class BO(Exception):pass
def R(d,a,be,pl):
 global ND,b,c,e
 ND+=1
 if ND>=12e4:raise BO
 if H.get(b,0)>1:return 50
 if d<=0:
  if pl>16:return E()
  st=E()
  if st>=be:return be
  if st>a:a=st
 lg=0
 for m in O(G(d<=0),pl):
  o=M(m)
  if o:
   lg+=1
   sc=-R(max(d-1,0),-be,-a,pl+1)
   b,c,e=o
   if sc>a:a=sc
   if a>=be:K[pl]=m;return be
 if d>0 and not lg:return -1e9+pl if A(b.index('K')) else 0
 return a
def T():
 global ND,b,c,e
 ND=0
 lg=[]
 for m in G(0):
  o=M(m)
  if o:lg.append(m);b,c,e=o
 if len(lg)<2:return lg[0]if lg else 0
 sc=[(0,m) for m in lg]
 bs=lg[0]
 try:
  for d in range(40):
   al=-1e9
   ns=[]
   ib=sc[0][1]
   for _,m in sc:
    o=M(m)
    v=-R(d-1,-1e9,-al,1)
    b,c,e=o
    ns+=[(-v,m)]
    if v>al:al=v;ib=m
   sc=sorted(ns)
   bs=ib
 except BO:pass
 return bs
def U(m):
 i=(m>>7)&127;j=m&127;pr=m>>14
 if RT:i,j=119-i,119-j
 return '%c'*4%(i%10+96,58-i//10,j%10+96,58-j//10)+(chr(pr+32)if pr else'')
def p(a,d):
 return json.load(u.urlopen(os.getenv('MAKEFUN_ENV_URL')+a,json.dumps(d).encode()))
while 1:
 g=p('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  F(g['fen'])
  m=U(T())
  L=g['legal_moves']
  if m not in L:m=L[0]
  g=p('/move',{'game':g['game'],'move':m})
