from latinsquare import LatinSquare
from alphabet import chars
from passphrase import Passphrase

a = chars('a','z')+chars('0','9')+list('-/:;()$&@".,?!')
s = LatinSquare(len(a)).dictionary(a)
s.mix(Passphrase('this/is/test/pa$$phrase',a).gen_lambda())
print(s)
for i in range(1,10):
	input = 'github.com'+str(i)
	print(input, s.get(input))

'''
example output:

9$4a.8;1f&)6/?mc3ky@rue:0tlph"bgd2-,nsj(5!viwxqo7z
;-hs:arx3/,$dmg6(9p"1.2!lqtibeuv5c8kfnzj4w&o7?y@)0
,cd-b$k;sgw2v1xen)ti9h@uj0zq5o4?&"67a83f/.my:rlp!(
z:c78w0tk@3."ypu9jv5l-haxm?&64$ieb!(,)r;2so/nqgdf1
:ome/"!76rbi1,kp$.(lw&qdsfnjgtv9xy@uc28-?5;z4)30ha
lw$,s)ty;ej!2io:r0/hqaunmvgd-b8@c.7z9kx16f"53p&4(?
upx@vo.!294y;7)qcbfz:gl&8sa3?0m,rtihe"$61/k(dwnj5-
s5ibehn3:t-dqjz/!armf"v2,9k1og@0y&48.u7wpclx6(;?$)
3b":6.(z7pshilt4)f?&jcd$;1rme/2qo5unw!k,@-yg80xva9
n4ou2bf(!q85yz0dws1g3e&ck;9x@v"lp/ha:.)7i6t?$jrm-,
5l9yxq4bo7&0).:z@d8fh1(?c$6a;3r!,jt/ipe"kmwsgu-nv2
-&q5od8sbzcv0f3gu$k1ai?@w)79yxp(lm/6h4:.t"j;en,r2!
d0kq1t5hiwvz7u.jo/-n4r3x26c89f;:)(l&py"@,?!amb$sge
t7-kn,qpr2zwco@!1ldbys.fg&v58ua"6:)0;9?x$3e4(i/hjm
2?zvqgc$df@x38a15ewk6t;yu:.709ls(rm"/&h4jpn)i-!,ob
6gl/p&$84(emjsn?hc);-y1i:w!,trqfzxv25dub0o3k@a79".
!@g2dew)$1uoxk9i-:jt7/y5n3fzvq&;?p".6ca8m4r0h,(lbs
.i?"&@:wc;hpr),y6u30!vt/ans(mlgk1qob2e-$xd9j57fz48
r8bn!s1?(dk-5gv$j;iex:cwtyqou2.&46a93f0zh7/@)mp",l
"1(ml?ec&sirn$-;/@:)20kthub!j,z8f9xovg5d3qawy6.7p4
by1ogiu:ek5q9w7t2hnj.m0v-a8fxz?);lp4"@6cr&,3/!s(d$
w"vc527,-x.@?9;o8!zq)dp4f(30&y/rmie:$6sagh1lbkjtun
exjgtm26/no1f-8rd"!,cl9qb.uwzk0a3;?@&v45(ys7p$:)ih
v(709z&dq.?3:4hfygc8/ks;@e"6)a,b!njmtlipwru$152-xo
k658u-9rnv7c&x?2f,qo;b".zl0y4@hm/e$)sa(3d:gp!1tiwj
cm0&yv6-53"?(asx4279$qrp.!:)l;tnj1ged/bhzif,o8wk@u
8/y4@5anu06&l3(v.-9xsom"7,);p?ijtgd$bh!:qezr2fk1cw
1aufwnxmj5984v&-zro2?!67qpy@.c:/h$s;(3l0b)d",giekt
fh@.cu3jwya4p0l57nxv(2/69r;?"&etidbs!:,)o$qm-z1g8k
q)89fkyi1c076@"wxt5upn:3v/&4a.se$!,lr;m?-(2hjodbzg
j.2w-!zl,ofu@qybk(gd0$481?xvc56p"h:3)7;9eai&stm/nr
g3wzkjv/tuxf.54nqm2-&,a9o"@c78)h:s(?l0py!;b6rde$1i
4t;p?yhu@)/l,:!0"5a3bxjm6-$sr(1wkzqdoi2e9g7nv.8f&c
i9n1jro"m-qk82c,gpb!@(7zd45ufw36a);y?x&vs0$.leh:t/
&j)l;0/5y:m(!hb3pv6ad9nr"2e$,skuwfzgqtoi71.-x4c8?@
o;fxz1@eg8y9ac6kviuw"j)05h4.37($s,rpm?/&nl-:t2b!qd
7e&64c)k8?:"m;r@aw0y,5ih3j(l/pd1go2!-$nsvbxtu9zq.f
$vtdi/-ahj2gznfmb6,r8pxo!7wkq1y30?&c45.ul@(9"s);e:
adph"4sf.l$/t(j&:8;?n@ge)k,rimozqv5-ubw!y201c39x67
@r3?0x"2vap;s6$9&o.7ez,l4bh:()j-nk1igmd/ft8!qcuwy5
)2/$h6,9am!egr1"s7lpk4ob(zjtdi5xv@cw8-fn&u?q.;0y:3
0!6)a7lq9"(:epi.;z&4t8bs?gm/$h-o2uwjk,1rcn@dfyv53x
hqrimpb.",dtk!wle4s(u?zg$8-n1jx790y5@oc2;v)f&:a3/6
?n:()3mv0hrsb/dalx"6g7-,poie!$w5u8f1zjqt.k429&@c;y
xs.37f?gz4;ah&/801@cmw$)yip":6!db-nrj(tlu,5ekvo29q
pksr(;i@?$t,-e2)myh:o3wj/5dbn!fc879qx1vgaz6u0"4.l&
(ue!$:j0)inbotqh,3m/z65-rx1g2dcy@4.f7w9k"8pval?&s;
y,a;39pox6l)$"e7?q4.if!(&d/hs:n2-wkt1rgm8jcbz@5u0v
mf!j,(g&lb1nud5st?e$v)8ki@o2w-74.a3x0zyq:9hc;/"6rp
/z,trld4p!gjwbu(i&$s5;f1ec2-kn9.730vyq@o)x:8?h6am"

github.com1 "pvawln8xx4
github.com2 etj!"i9ux/3
github.com3 ch?e04(,z)i
github.com4 /90,"vw,we,
github.com5 uw(gno;7m4)
github.com6 05pj5hel4ej
github.com7 ludi"x2r("m
github.com8 z?y4a0"z?tl
github.com9 2h@:$h382p/
'''

