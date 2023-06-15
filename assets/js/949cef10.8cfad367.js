"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[439],{3905:(e,t,a)=>{a.d(t,{Zo:()=>c,kt:()=>d});var r=a(7294);function n(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,r)}return a}function s(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){n(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,r,n=function(e,t){if(null==e)return{};var a,r,n={},i=Object.keys(e);for(r=0;r<i.length;r++)a=i[r],t.indexOf(a)>=0||(n[a]=e[a]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)a=i[r],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var l=r.createContext({}),p=function(e){var t=r.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):s(s({},t),e)),a},c=function(e){var t=p(e.components);return r.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},h=r.forwardRef((function(e,t){var a=e.components,n=e.mdxType,i=e.originalType,l=e.parentName,c=o(e,["components","mdxType","originalType","parentName"]),h=p(a),d=n,m=h["".concat(l,".").concat(d)]||h[d]||u[d]||i;return a?r.createElement(m,s(s({ref:t},c),{},{components:a})):r.createElement(m,s({ref:t},c))}));function d(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=a.length,s=new Array(i);s[0]=h;var o={};for(var l in t)hasOwnProperty.call(t,l)&&(o[l]=t[l]);o.originalType=e,o.mdxType="string"==typeof e?e:n,s[1]=o;for(var p=2;p<i;p++)s[p]=a[p];return r.createElement.apply(null,s)}return r.createElement.apply(null,a)}h.displayName="MDXCreateElement"},54:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>s,default:()=>u,frontMatter:()=>i,metadata:()=>o,toc:()=>p});var r=a(7462),n=(a(7294),a(3905));const i={},s="Cheat-sheet",o={unversionedId:"Netzwerke/apis",id:"Netzwerke/apis",title:"Cheat-sheet",description:"What is an API?",source:"@site/docs/Netzwerke/apis.md",sourceDirName:"Netzwerke",slug:"/Netzwerke/apis",permalink:"/EF-Informatik/docs/Netzwerke/apis",draft:!1,editUrl:"https://github.com/Grashaum/EF-Informatik/tree/main/docs/Netzwerke/apis.md",tags:[],version:"current",frontMatter:{},sidebar:"defaultSidebar",previous:{title:"LERNZIELE",permalink:"/EF-Informatik/docs/Netzwerke/Lernziele"},next:{title:"login-cookies",permalink:"/EF-Informatik/docs/Netzwerke/login-cookies"}},l={},p=[{value:"What is an API?",id:"what-is-an-api",level:3},{value:"JSON Format (JavaScript Object Notation)",id:"json-format-javascript-object-notation",level:3},{value:"XML Format (Extensible Markup Language)",id:"xml-format-extensible-markup-language",level:3},{value:"HTTP Request:",id:"http-request",level:3},{value:"HTTP Status Codes",id:"http-status-codes",level:3},{value:"Polling",id:"polling",level:3}],c={toc:p};function u(e){let{components:t,...i}=e;return(0,n.kt)("wrapper",(0,r.Z)({},c,i,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"cheat-sheet"},"Cheat-sheet"),(0,n.kt)("h3",{id:"what-is-an-api"},"What is an API?"),(0,n.kt)("p",null,"APIs (application programming interfaces)"),(0,n.kt)("p",null,"An API is the tool that makes a website's data digestible for a computer. Through it, a computer can view and edit data, just like a person can by loading pages and submitting forms. APIs make it easy to share data between two systems."),(0,n.kt)("p",null,"API is provided by the server."),(0,n.kt)("p",null,"When one site pulls in data from the other, the site providing the data is acting as the server, and the site fetching the data is the client."),(0,n.kt)("h3",{id:"json-format-javascript-object-notation"},"JSON Format (JavaScript Object Notation)"),(0,n.kt)("p",null,"List with values that have names"),(0,n.kt)("p",null,"JSON is a very simple format that has two pieces:"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},"Key: an attribute about an object (size, toppings...)"),(0,n.kt)("li",{parentName:"ul"},"Value: the value of an attribute (small, pepperoni...)")),(0,n.kt)("h3",{id:"xml-format-extensible-markup-language"},"XML Format (Extensible Markup Language)"),(0,n.kt)("p",null,'XML always starts with a root node inside the order are more "child" nodes. '),(0,n.kt)("p",null,(0,n.kt)("img",{src:a(7661).Z,width:"651",height:"377"}),"\nThe XML format requires a lot more text to communicate than JSON does.\n###HTTPS"),(0,n.kt)("p",null,"This works the same as HTTP. The difference being the S standing for secure."),(0,n.kt)("h3",{id:"http-request"},"HTTP Request:"),(0,n.kt)("p",null,"Communication in HTTP centers around a concept called the Request-Response Cycle. The client sends the server a request to do something. The server, in turn, sends the client a response saying whether or not the server could do what the client asked."),(0,n.kt)("p",null,"The client has to include the following things:"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("p",{parentName:"li"},"URL"),(0,n.kt)("p",{parentName:"li"},"A unique address for a thing. official name: resource"),(0,n.kt)("p",{parentName:"li"},"Url's are a easy way for the cloent to tell the server which thin it wants to interact with.")),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("p",{parentName:"li"},"Methods"),(0,n.kt)("p",{parentName:"li"},"GET - Asks the server to retrieve a resource"),(0,n.kt)("p",{parentName:"li"},"POST - Asks the server to create a new resource. They always have a body & headers (as described below)"),(0,n.kt)("p",{parentName:"li"},"PUT - Asks the server to edit/update an existing resource. The entire resource gets changed."),(0,n.kt)("p",{parentName:"li"},"DELETE - Asks the server to delete a resource")),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("p",{parentName:"li"},"Headers"),(0,n.kt)("p",{parentName:"li"},"They provide meta-information about a request. They are a simple list of items like the time the client sent the request and the size of the request body.")),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("p",{parentName:"li"},"Body"),(0,n.kt)("p",{parentName:"li"},"The request body contains the data the client wants to send the server. This is the only part of the request the client has complete control over ."))),(0,n.kt)("p",null,(0,n.kt)("img",{src:a(449).Z,width:"938",height:"631"})),(0,n.kt)("p",null,"The response headers and body follow the same format as requests."),(0,n.kt)("h3",{id:"http-status-codes"},"HTTP Status Codes"),(0,n.kt)("p",null,"Status codes are three-digit numbers that each have a unique meaning. When used correctly in an API, this little number can communicate a lot of info to the client. For example, you may have seen this page during your internet wanderings."),(0,n.kt)("h3",{id:"polling"},"Polling"),(0,n.kt)("p",null,"Polling is a way to keep the client updated about what is happening on the website or with the data they requested.\nThe more frequently the client makes requests (polls), the closer the client gets to real-time communication."),(0,n.kt)("p",null,"An API defines endpoints so the https so they lead the client to the right address."))}u.isMDXComponent=!0},449:(e,t,a)=>{a.d(t,{Z:()=>r});const r=a.p+"assets/images/http-7b29cf888e3d1ee4a1555c1c86984a76.PNG"},7661:(e,t,a)=>{a.d(t,{Z:()=>r});const r=a.p+"assets/images/node-1aa597de64af956c226aa939733a3846.PNG"}}]);