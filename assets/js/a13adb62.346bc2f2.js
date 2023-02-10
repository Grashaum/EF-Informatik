"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[737],{3905:(e,n,t)=>{t.d(n,{Zo:()=>d,kt:()=>h});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function s(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function l(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var o=r.createContext({}),u=function(e){var n=r.useContext(o),t=n;return e&&(t="function"==typeof e?e(n):s(s({},n),e)),t},d=function(e){var n=u(e.components);return r.createElement(o.Provider,{value:n},e.children)},c={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},p=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,o=e.parentName,d=l(e,["components","mdxType","originalType","parentName"]),p=u(t),h=i,m=p["".concat(o,".").concat(h)]||p[h]||c[h]||a;return t?r.createElement(m,s(s({ref:n},d),{},{components:t})):r.createElement(m,s({ref:n},d))}));function h(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,s=new Array(a);s[0]=p;var l={};for(var o in n)hasOwnProperty.call(n,o)&&(l[o]=n[o]);l.originalType=e,l.mdxType="string"==typeof e?e:i,s[1]=l;for(var u=2;u<a;u++)s[u]=t[u];return r.createElement.apply(null,s)}return r.createElement.apply(null,t)}p.displayName="MDXCreateElement"},7179:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>o,contentTitle:()=>s,default:()=>c,frontMatter:()=>a,metadata:()=>l,toc:()=>u});var r=t(7462),i=(t(7294),t(3905));const a={},s="Finaler Blog-Beitrag",l={permalink:"/EF-Informatik/finaler game-blog",editUrl:"https://github.com/Grashaum/EF-Informatik/tree/main/blog/finaler game-blog.md",source:"@site/blog/finaler game-blog.md",title:"Finaler Blog-Beitrag",description:"Ziel des Spiels",date:"2023-02-10T14:16:49.000Z",formattedDate:"10. Februar 2023",tags:[],readingTime:1.01,hasTruncateMarker:!1,authors:[],frontMatter:{},prevItem:{title:"Numtrip-blog",permalink:"/EF-Informatik/Numtrip-blog"},nextItem:{title:"wiedereinstieg-python",permalink:"/EF-Informatik/2022/08/26/wiedereinstieg-python"}},o={authorsImageUrls:[]},u=[{value:"Ziel des Spiels",id:"ziel-des-spiels",level:2},{value:"Voraussetzung",id:"voraussetzung",level:2},{value:"Erkl\xe4rung eines algorithmischen Konzepts",id:"erkl\xe4rung-eines-algorithmischen-konzepts",level:2},{value:"Gr\xf6sste Herausforderungen",id:"gr\xf6sste-herausforderungen",level:2},{value:"Tipps",id:"tipps",level:2}],d={toc:u};function c(e){let{components:n,...a}=e;return(0,i.kt)("wrapper",(0,r.Z)({},d,a,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"ziel-des-spiels"},"Ziel des Spiels"),(0,i.kt)("p",null,"Unterhaltung:) "),(0,i.kt)("p",null,"das finale Ziel ist es, 2048 Punkte zu erreichen.\nDas geht dadurch, dass die Zahlen immer adddiert werden wenn sie angeklickt werden.\nMit etwas strategie kann man die immer h\xf6heren Zahlen addieren. Es gibt jedoch die Einschr\xe4nkung, dass man ein Feld nur ausw\xe4hlen kann, wenn ein benachbartes Feld den Gleichen Wert hat."),(0,i.kt)("h2",{id:"voraussetzung"},"Voraussetzung"),(0,i.kt)("p",null,"Was muss ich installieren, um das Spiel zu starten?\nPython (version 3.1) Damit der syntax funktioniert."),(0,i.kt)("h2",{id:"erkl\xe4rung-eines-algorithmischen-konzepts"},"Erkl\xe4rung eines algorithmischen Konzepts"),(0,i.kt)("p",null,"In meinem spiel habe ich das Ende so definiert, dass man gewonnen hat wenn man auf einem Feld hundert erreicht hat. Daf\xfcr muss das Programm nach jeder Runde \xfcberpr\xfcfen ob eine der Zellen das Ziel schon erreicht hat. Solange die Funktion Spielende False r\xfcckmeldet, geht das Spiel weiter.\n",(0,i.kt)("img",{src:t(2060).Z,width:"583",height:"225"})),(0,i.kt)("h2",{id:"gr\xf6sste-herausforderungen"},"Gr\xf6sste Herausforderungen"),(0,i.kt)("p",null,"Obschon wir sehr viel unterst\xfctzung und Beispiel-codes zur verf\xfcgung hatten, war unsere eigene Kreativit\xe4t und know-how gefragt und da dies nicht immer vorhanden war, habe ich viel unterst\xfctzung gebraucht vom Lehrer und verschiedenen Kollegen, die mehr erfahrung haben als ich.\n(Das zurechtfinden mit den verschiedenen Tools ging sehr schnell.)"),(0,i.kt)("h2",{id:"tipps"},"Tipps"),(0,i.kt)("p",null,"(f\xfcr andere EF-Sch\xfcler:innen, die das Spiel auch umsetzen m\xf6chten)\nUngeniert Fragen stellen und mit Mitsch\xfcler:innen austauschen f\xfcr individuelle L\xf6sungs-ans\xe4tze."))}c.isMDXComponent=!0},2060:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/Spielende-35a9e47d53fd1023986fa67df495a5c7.PNG"}}]);