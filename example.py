from latinsquare import LatinSquare
from alphabet import chars
import random

a = chars('a','z')+chars('0','9')+list('-/:;()$&@".,?!')
s = LatinSquare(len(a)).dictionary(a)
s.mix(lambda cur,size: random.randint(cur,size-1))
print(s)
for i in range(1,10):
	input = 'github.com'+str(i)
	print(input, s.get(input))

'''
example output:

4i@gw:pk$o2qby7tj!h5c&e3()9l;8daxn,"zuf-?1rv0/.sm6
s-oq".n?h56w2m8y$7)p4jbzv3dkxe&1:/clr!@9ut0a;g,fi(
vptdjbi)"y.&:o0@wrlm(qx?ck/h8;gse-6$uz1n3f!4792a5,
g3"7e5?6:li8mh1$xa.k/;yc9,r2@t0&ounb4vwz(jsdf!pq)-
p$g?!f"e0qtu1&(dr6;w5za:mx)84v3-slo7.2/hb9,ick@njy
6oa-d8y$q1x9;fzsg3wt2/0l."pj!rnc7mb&k)v5h4?,uie(@:
)er,4&x@a0wcq7n!vp1;h(gylt2f9/6?d:$sm5zbouik-.j38"
any&$2-3lm,j.5;o"0kivw:u4?g)exqfb9(h!rt/z@7s8d61pc
/)w!8ok2x"m7y$aj;v:ln0t,-.zbf1rd@?pec(q36&49su5ghi
cmf/qx5lj@bget!1&u$o,d8)6h-"079v;p.w3?sikaz(rn:4y2
"0?b6/7acud29zm3,y4!w.-fjsxvpi:hn8q(@tk;1)o$5eglr&
;v.@534/i,uo?6"2mw-c0ykd791nhlte)srp&q:agbj8$fzx(!
yq-h3v&0u9s)4/.n?:!dtkc8@7"r6,l5(j1zexiw;pbo2$amgf
i"d3r1$x7&@zfqcg!,8jmusb5ek;v4?nahy02.9l:/6p()t-wo
l;u2(g814!&6drizcms7",9@$f:an-.)/ewvoy?xt35hpbqk0j
qzl8bpu(.k-ei)th:1,?gxm4dc06oy;j5!/2sa"rv$f&@7nw39
?:7(awbyf8$vj;90s-@ek4&5)o,tgdczq2l1pi!.mrn3/6"uxh
h8z.cd;fvrq,g!pu(5a0$6/t"1bs-n2k9xj4yo3e@?mli:&)7w
5j/kusw8rg1?ad69z20qo3vxy;h7c()i4"@!:bn$e-.m,lfp&t
,ysng;o"&fe/81uad?j@.97h2$iwr!-(05:q)k4mlv36zpxctb
:1c5nrfq947p!vk(-ldsxiuje&yg3?m2z@;/$",tw6hb)o0.a8
j!)x.-r463/:n?ok2@(z&bpaqv8cm5e"i0d,1fh7sltwy;9$ug
kx!6vqets7j(&0-r4if8lcdoh@.1/9,3gb"a5mu:yzp)n2w?;$
2@vi97tjga;-0s34/)q1bnr":w5&uzp,!yedlh(o$ck.?m86fx
bf(m-!1&/v0ir4)cnhgaepzwxqod?35.ut89"$6@j,l:ky72s;
u.8v1"2m@eha$xd;f9ob?sjp35cyq&4rw6ktn-7,i0/zg(l!:)
es6yiuadn(rmzch,p$/v853q;g@9k)o:?17-wj2f&."xlt!b40
842tm?v9p6zy3,$.5jn(7o)g0/f-lh@xka!iq&bsd:w;"1uecr
9kjr;y).e$50o"sw84bh-7@6n2u:1f!gt3ix(c&?,qv/azmdlp
@dp"kcg!3nvl(-bi)ez/fh601rju.2$y,qs?;85&7mxt:w4o9a
7cb1yk(-523t).j:o&p6!@h/rnsi"$f;lvumgde49xq0wa?8,z
r6xs@h,py:kflbqetgm.z1"-uiv5jwa7$c3o9/;(n8d!&4)02?
1/mjh69zkic$,px5l;?-a".!suq3b:w@2dv)70ygro8fe&(tn4
.t4p/0@wds8n7a?v9k&f:-!$bjmqzui6roxghlcy"()235;,1e
z2;4f$.5txls"eg81/y:3awi?m(o&qv!j,)@-n06p79udchrbk
d?$0xm3,bhp;5lf"es2)98o(/6!.t@7qyz-:v4jucwag1ri&kn
-l&z0th:8jor@w4q7ce$i!f2pb?xasu/1)m;6,dk.g(nv3y9"5
0(:fo)cnm.?@k2wbyqi,rtl9!-ap$"18h4z5dgxv/e&7js3;6u
(519&emhwt:dx@rfqz"y6g;k,ln$70/48i2j?3ap)suc!-bvo.
3b0csj:o1;"4w8/7antx)vqmky6@dg(u&.hfipr25!-?9,$zel
wrke2n!v,?9b-3y).tcuq:is&4;(5mx$p7g6f1l0ah@jo8/"zd
tgi$)(dr?-4hcn:pkxu91l,7f!wz2."o6&a38;mq05e@bjvy/s
f95wl,/u)p("6iemh83ns$2raz&?:bjt.g4k07od!y;1xqc@-v
&uh;:izc2)nxpk@lbf63de5vg(7,yo8wmr9.as$!4"1qt0-j?/
mw9)zaj;!df3sg,/u.7&y?4eo8l0(ckpv$trb:-"xn256h1iq@
xa,opzsg-c!5u(l6i"94;m?&8dt/)kyb3f0njw.1q2$eh@r:v7
o&nl?4q7z/akv92-3brg@)(;t0$!,6hmcwfuxepj8i:y."s5d1
!,eatl6iob)1h:&x@d52uf$nzp4mwjs0"(?y/98c-;grqvk7.3
nhqu7@lb;wy!tjv&0(x"pr1.i:3esaz9fk58,6g)2dc-4?o/$m
$73:,90s(zg./u5?6ovrj2n1wae4ipbl-;&ct@)8fky"mxdh!q

github.com1 @u:n?1ot87k
github.com2 r6$-j:1k27g
github.com3 n&aa-4rzhk1
github.com4 v2ynv@6k8@$
github.com5 6q9edj:zm(r
github.com6 /(a7y9m@dnq
github.com7 "c0fk51-zz5
github.com8 f4wmi:4kb5p
github.com9 f?5we?-3,je
'''

