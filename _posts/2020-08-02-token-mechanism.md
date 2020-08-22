---
layout: post
title: "Token的使用"
tags: Java Token
author: Shenpotato
catalog: true
---



> Token与Session比较 + Shiro整合Springboot实现登陆校验
>
> 参考：
>
> 彻底理解cookie、session和token https://mp.weixin.qq.com/s/e3Sy4Mw69gN1weHXc7KsFA
>
> SpringBoot+Shiro+Jwt实现登录认证 https://www.jianshu.com/p/9b6eb3308294
>
> SpringBoot+vue前后端分离博客项目 https://juejin.im/post/6844903823966732302#heading-6
>
> 项目代码：
>
> https://github.com/Shenpotato/vueblog



项目中使用到了Shrio整合Springboot进行JwtToken验证，自己对这块内容不是太熟悉，进行一点记录





### 一、Cookie、 Session以及Token的比较



#### 1. Cookie

cookie是指浏览器中永久存储的数据，仅代表浏览器实现的数据存储功能。

cookie由服务器生成，发送给浏览器，浏览器把cookie以kv形式保存到某个目录下的文本文件内，下一次请求同一网站时会把该cookie发送给服务器。由于cookie是存在客户端上的，所以浏览器加入了一些限制确保cookie不会被恶意使用，同时不会占据太多磁盘空间，所以每个域的cookie数量是有限的。



#### 2. Session以及Session 的缺点

在服务器和客户端进行交互时，需要识别客户端的身份。

服务端通过给客户端分配不同的标识，称为sessionId。客户端在每次向服务端发送请求时，都带上这个标识，使得服务端识别出不同的客户端。

默认浏览器客户端的sessionId保存在cookie中。同样，服务端需要保存sessionId在服务器上。这样存在几个问题：

- Session在用户请求量大的时候服务器的开销过大
- Session不利于搭建服务器的集群（进行负载均衡时，请求到另一台服务器的时候Session会丢失）



**基于服务器验证方式的问题**（Session是最常见的基于服务器验证的方式）

1. **Seesion：**每次认证用户发起请求时，服务器需要去创建一个记录来存储信息。当越来越多的用户发请求时，内存的开销也会不断增加。
2. **可扩展性：**在服务端的内存中使用Seesion存储登录信息，伴随而来的是可扩展性问题。
3. **CORS(跨域资源共享)：**当我们需要让数据跨多台移动设备上使用时，跨域资源的共享会是一个让人头疼的问题。在使用Ajax抓取另一个域的资源，就可以会出现禁止请求的情况。
4. **CSRF(跨站请求伪造)：**用户在访问银行网站时，他们很容易受到跨站请求伪造的攻击，并且能够被利用其访问其他的网站。

在这些问题中，可扩展行是最突出的。因此我们有必要去寻求一种更有行之有效的方法。



#### **3. Token**

##### 3.1 客户端和服务器端交互流程

**基于Token的验证方式：**

1. 用户登录校验，校验成功后就返回Token给客户端。
2. 客户端收到数据后保存在客户端
3. 客户端每次访问API是携带Token到服务器端。
4. 服务器端采用filter过滤器校验。校验成功则返回请求数据，校验失败则返回错误码。

每一次请求都需要token。token应该在HTTP的头部发送从而保证了Http请求无状态。我们同样通过设置服务器属性Access-Control-Allow-Origin:* ，让服务器能接受到来自所有域的请求。

需要主要的是，在ACAO头部标明(designating)*时，不得带有像HTTP认证，客户端SSL证书和cookies的证书。

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghgw4x1gboj30hr0ejjrv.jpg)



##### **3.2 原理**

以**JwtToken**为例，其包含三部分：

1. Header

   存储两个变量：

   - 密钥
   - 算法（将Header和Payload加密成Signature的算法）

2. Payload

   基本信息如下：

   - 签发人：这个”Token“的所属者。一般是userId
   - 创建时间
   - 失效时间
   - 唯一标识：使用算法生成的唯一标识

3. Signature

   由Header中的算法加密Header和Payload产生，用于比对信息，防止纂改Header和Payload。

再将这三个部分的信息经过加密生成一个JwtToken的字符串，发送给客户端，客户端保存在本地。在服务端进行验证。

验证方式是在服务端进行一次相同算法和密钥的计算，比较得出的Token和传输过来的Token。通过这种方式，服务端就无需保存sessionId，只生成Token，然后验证Token。简而言之，使用CPU计算计算换取Session的存储空间。



##### **3.3 Token的优势**

**无状态、可扩展**

在客户端存储的Tokens是无状态的，并且能够被扩展。基于这种无状态和不存储Session信息，负载负载均衡器能够将用户信息从一个服务传到其他服务器上。

如果我们将已验证的用户的信息保存在Session中，则每次请求都需要用户向已验证的服务器发送验证信息(称为Session亲和性)。用户量大时，可能会造成一些拥堵。

但是不要着急。使用tokens之后这些问题都迎刃而解，因为tokens自己hold住了用户的验证信息。

**安全性**

请求中发送token而不再是发送cookie能够防止CSRF(跨站请求伪造)。即使在客户端使用cookie存储token，cookie也仅仅是一个存储机制而不是用于认证。不将信息存储在Session中，让我们少了对session操作。

token是有时效的，一段时间之后用户需要重新验证。我们也不一定需要等到token自动失效，token有撤回的操作，通过token revocataion可以使一个特定的token或是一组有相同认证的token无效。

**可扩展性**

Tokens能够创建与其它程序共享权限的程序。例如，能将一个随便的社交帐号和自己的大号(Fackbook或是Twitter)联系起来。当通过服务登录Twitter(我们将这个过程Buffer)时，我们可以将这些Buffer附到Twitter的数据流上(we are allowing Buffer to post to our Twitter stream)。

使用tokens时，可以提供可选的权限给第三方应用程序。当用户想让另一个应用程序访问它们的数据，我们可以通过建立自己的API，得出特殊权限的tokens。

**多平台跨域**

我们提前先来谈论一下CORS(跨域资源共享)，对应用程序和服务进行扩展的时候，需要介入各种各种的设备和应用程序。



### 二、Springboot整合Shiro



#### 1. 流程

##### 1.1 shiro 验证流程

- 客户端发起请求，shiro过滤器生效，判断是否是login或者logout请求
- 是则执行请求，如果不是则进入JwtFilter。

##### 1.2 JwtFilter验证流程

- 请求不携带token（Authorization键），则在JwtFilter处抛出异常/返回未登录，让它去登录

- 请求携带token，则在JwtFilter中获取jwt，封装成JwtToken对象。

- 使用subject执行login()方法进行校验，这个方法调用了创建的JwtRealm中的认证方法。

- 使用JwtUtil.isVerify(jwt)判断是否通过。



#### 2. 环境搭建

由于我们需要对shiro的SecurityManager进行设置，所以不能使用shiro-spring-boot-starter进行与springboot的整合，只能使用spring-shiro。

```
<!-- 自动依赖导入 shiro-core 和 shiro-web -->
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.4.1</version>
</dependency>
```

在具体的项目中，考虑到后面的集群和负载均衡，我们需要使用会话共享。考虑用redis来存储这些数据，所以也需要整合redis。因此，使用了shiro-redis这样一个starter进行配置。下面包含了hutool工具和jwt的工具包。

```
<dependency>
    <groupId>org.crazycake</groupId>
    <artifactId>shiro-redis-spring-boot-starter</artifactId>
    <version>3.2.1</version>
</dependency>
<!-- hutool工具类-->
<dependency>
    <groupId>cn.hutool</groupId>
    <artifactId>hutool-all</artifactId>
    <version>5.3.3</version>
</dependency>
<!-- jwt -->
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
```

yml文件信息配置：

```
shiro-redis:
  enabled: true
  redis-manager:
    host: 127.0.0.1:6379
markerhub:
  jwt:
    # 加密秘钥
    secret: f4e2e52034348f86b67cde581c0f9eb5
    # token有效时长，7天，单位秒
    expire: 604800
    header: token
```

项目有使用spring-boot-devtools，需要添加一个配置文件，在resources目录下新建文件夹META-INF，然后新建文件spring-devtools.properties，这样热重启时候才不会报错。

- resources/META-INF/spring-devtools.properties

```
restart.include.shiro-redis=/shiro-[\\w-\\.]+jar
```



#### 3. 类介绍

在流程中，出现了一些校验所需要编写的类，大致的实现逻辑对应关系也如下。

##### 3.1 JwtUtil

JwtUtil作为一个工具类，主要需要实现：

- 对于信息的加密，生成JwtToken
- 对于信息的解密，解析JwtToken
- 判断解析出的Token是否合法：包括头部和荷载部分有没有被纂改，以及是否过期。

项目中也存在一个JwtUtils的类位于util包下，功能与下述代码一致，实现方法略有不同。

```
package cn.coderymy.util;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.apache.commons.codec.binary.Base64;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
/*
* 总的来说，工具类中有三个方法
* 获取JwtToken，获取JwtToken中封装的信息，判断JwtToken是否存在
* 1. encode()，参数是=签发人，存在时间，一些其他的信息=。返回值是JwtToken对应的字符串
* 2. decode()，参数是=JwtToken=。返回值是荷载部分的键值对
* 3. isVerify()，参数是=JwtToken=。返回值是这个JwtToken是否存在
* */
public class JwtUtil {
    //创建默认的秘钥和算法，供无参的构造方法使用
    private static final String defaultbase64EncodedSecretKey = "badbabe";
    private static final SignatureAlgorithm defaultsignatureAlgorithm = SignatureAlgorithm.HS256;

    public JwtUtil() {
        this(defaultbase64EncodedSecretKey, defaultsignatureAlgorithm);
    }

    private final String base64EncodedSecretKey;
    private final SignatureAlgorithm signatureAlgorithm;

    public JwtUtil(String secretKey, SignatureAlgorithm signatureAlgorithm) {
        this.base64EncodedSecretKey = Base64.encodeBase64String(secretKey.getBytes());
        this.signatureAlgorithm = signatureAlgorithm;
    }

    /*
     *这里就是产生jwt字符串的地方
     * jwt字符串包括三个部分
     *  1. header
     *      -当前字符串的类型，一般都是“JWT”
     *      -哪种算法加密，“HS256”或者其他的加密算法
     *      所以一般都是固定的，没有什么变化
     *  2. payload
     *      一般有四个最常见的标准字段（下面有）
     *      iat：签发时间，也就是这个jwt什么时候生成的
     *      jti：JWT的唯一标识
     *      iss：签发人，一般都是username或者userId
     *      exp：过期时间
     *
     * */
    public String encode(String iss, long ttlMillis, Map<String, Object> claims) {
        //iss签发人，ttlMillis生存时间，claims是指还想要在jwt中存储的一些非隐私信息
        if (claims == null) {
            claims = new HashMap<>();
        }
        long nowMillis = System.currentTimeMillis();

        JwtBuilder builder = Jwts.builder()
                .setClaims(claims)
                .setId(UUID.randomUUID().toString())//2. 这个是JWT的唯一标识，一般设置成唯一的，这个方法可以生成唯一标识
                .setIssuedAt(new Date(nowMillis))//1. 这个地方就是以毫秒为单位，换算当前系统时间生成的iat
                .setSubject(iss)//3. 签发人，也就是JWT是给谁的（逻辑上一般都是username或者userId）
                .signWith(signatureAlgorithm, base64EncodedSecretKey);//这个地方是生成jwt使用的算法和秘钥
        if (ttlMillis >= 0) {
            long expMillis = nowMillis + ttlMillis;
            Date exp = new Date(expMillis);//4. 过期时间，这个也是使用毫秒生成的，使用当前时间+前面传入的持续时间生成
            builder.setExpiration(exp);
        }
        return builder.compact();
    }

    //相当于encode的方向，传入jwtToken生成对应的username和password等字段。Claim就是一个map
    //也就是拿到荷载部分所有的键值对
    public Claims decode(String jwtToken) {

        // 得到 DefaultJwtParser
        return Jwts.parser()
                // 设置签名的秘钥
                .setSigningKey(base64EncodedSecretKey)
                // 设置需要解析的 jwt
                .parseClaimsJws(jwtToken)
                .getBody();
    }

    //判断jwtToken是否合法
    public boolean isVerify(String jwtToken) {
        //这个是官方的校验规则，这里只写了一个”校验算法“，可以自己加
        Algorithm algorithm = null;
        switch (signatureAlgorithm) {
            case HS256:
                algorithm = Algorithm.HMAC256(Base64.decodeBase64(base64EncodedSecretKey));
                break;
            default:
                throw new RuntimeException("不支持该算法");
        }
        JWTVerifier verifier = JWT.require(algorithm).build();
        verifier.verify(jwtToken);  // 校验不通过会抛出异常
        //判断合法的标准：1. 头部和荷载部分没有篡改过。2. 没有过期
        return true;
    }
 }
```



#### 3.2 JwtFilter

```
/*
 * 自定义一个Filter，用来拦截所有的请求判断是否携带Token
 * isAccessAllowed()判断是否携带了有效的JwtToken
 * onAccessDenied()是没有携带JwtToken的时候进行账号密码登录，登录成功允许访问，登录失败拒绝访问
 * */
@Slf4j
public class JwtFilter extends AccessControlFilter {
    /*
     * 1. 返回true，shiro就直接允许访问url
     * 2. 返回false，shiro才会根据onAccessDenied的方法的返回值决定是否允许访问url
     * */
    @Override
    protected boolean isAccessAllowed(ServletRequest request, ServletResponse response, Object mappedValue) throws Exception {
        log.warn("isAccessAllowed 方法被调用");
        //这里先让它始终返回false来使用onAccessDenied()方法
        return false;
    }

    /**
     * 返回结果为true表明登录通过
     */
    @Override
    protected boolean onAccessDenied(ServletRequest servletRequest, ServletResponse servletResponse) throws Exception {
        log.warn("onAccessDenied 方法被调用");
        //这个地方和前端约定，要求前端将jwtToken放在请求的Header部分

        //所以以后发起请求的时候就需要在Header中放一个Authorization，值就是对应的Token
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        String jwt = request.getHeader("Authorization");
        log.info("请求的 Header 中藏有 jwtToken {}", jwt);
        JwtToken jwtToken = new JwtToken(jwt);
        /*
         * 下面就是固定写法
         * */
        try {
            // 委托 realm 进行登录认证
            //所以这个地方最终还是调用JwtRealm进行的认证
            getSubject(servletRequest, servletResponse).login(jwtToken);
            //也就是subject.login(token)
        } catch (Exception e) {
            e.printStackTrace();
            onLoginFail(servletResponse);
            //调用下面的方法向客户端返回错误信息
            return false;
        }

        return true;
        //执行方法中没有抛出异常就表示登录成功
    }

    //登录失败时默认返回 401 状态码
    private void onLoginFail(ServletResponse response) throws IOException {
        HttpServletResponse httpResponse = (HttpServletResponse) response;
        httpResponse.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
        httpResponse.getWriter().write("login error");
    }
}
```



#### 3.3 JwtToken

```
//这个就类似UsernamePasswordToken
public class JwtToken implements AuthenticationToken {

    private String jwt;

    public JwtToken(String jwt) {
        this.jwt = jwt;
    }

    @Override//类似是用户名
    public Object getPrincipal() {
        return jwt;
    }

    @Override//类似密码
    public Object getCredentials() {
        return jwt;
    }
    //返回的都是jwt
}
```



#### 3.4 JwtRealm

创建判断jwt是否有效的认证方式的Realm

```
@Slf4j
public class JwtRealm extends AuthorizingRealm {
    /*
     * 多重写一个support
     * 标识这个Realm是专门用来验证JwtToken
     * 不负责验证其他的token（UsernamePasswordToken）
     * */
    @Override
    public boolean supports(AuthenticationToken token) {
        //这个token就是从过滤器中传入的jwtToken
        return token instanceof JwtToken;
    }

    //授权
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals) {
        return null;
    }    //认证
    //这个token就是从过滤器中传入的jwtToken
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) throws AuthenticationException {

        String jwt = (String) token.getPrincipal();
        if (jwt == null) {
            throw new NullPointerException("jwtToken 不允许为空");
        }
        //判断
        JwtUtil jwtUtil = new JwtUtil();
        if (!jwtUtil.isVerify(jwt)) {
            throw new UnknownAccountException();
        }
        //下面是验证这个user是否是真实存在的
        String username = (String) jwtUtil.decode(jwt).get("username");//判断数据库中username是否存在
        log.info("在使用token登录"+username);
        return new SimpleAuthenticationInfo(jwt,jwt,"JwtRealm");
        //这里返回的是类似账号密码的东西，但是jwtToken都是jwt字符串。还需要一个该Realm的类名

    }
}
```



#### 3.5 ShiroConfig

配置一些信息

- 因为不适用Session，所以为了防止会调用getSession()方法而产生错误，所以默认调用自定义的Subject方法
- 一些修改，关闭SHiroDao等
- 注册JwtFilter

```
@Configuration
public class ShiroConfig {
    /*
     * a. 告诉shiro不要使用默认的DefaultSubject创建对象，因为不能创建Session
     * */
    @Bean
    public SubjectFactory subjectFactory() {
        return new JwtDefaultSubjectFactory();
    }

    @Bean
    public Realm realm() {
        return new JwtRealm();
    }

    @Bean
    public DefaultWebSecurityManager securityManager() {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        securityManager.setRealm(realm());
        /*
         * b
         * */
        // 关闭 ShiroDAO 功能
        DefaultSubjectDAO subjectDAO = new DefaultSubjectDAO();
        DefaultSessionStorageEvaluator defaultSessionStorageEvaluator = new DefaultSessionStorageEvaluator();
        // 不需要将 Shiro Session 中的东西存到任何地方（包括 Http Session 中）
        defaultSessionStorageEvaluator.setSessionStorageEnabled(false);
        subjectDAO.setSessionStorageEvaluator(defaultSessionStorageEvaluator);
                securityManager.setSubjectDAO(subjectDAO);
        //禁止Subject的getSession方法
        securityManager.setSubjectFactory(subjectFactory());
        return securityManager;
    }

    @Bean
    public ShiroFilterFactoryBean shiroFilterFactoryBean() {
        ShiroFilterFactoryBean shiroFilter = new ShiroFilterFactoryBean();
        shiroFilter.setSecurityManager(securityManager());
        shiroFilter.setLoginUrl("/unauthenticated");
        shiroFilter.setUnauthorizedUrl("/unauthorized");
        /*
         * c. 添加jwt过滤器，并在下面注册
         * 也就是将jwtFilter注册到shiro的Filter中
         * 指定除了login和logout之外的请求都先经过jwtFilter
         * */
        Map<String, Filter> filterMap = new HashMap<>();
        //这个地方其实另外两个filter可以不设置，默认就是
        filterMap.put("anon", new AnonymousFilter());
        filterMap.put("jwt", new JwtFilter());
        filterMap.put("logout", new LogoutFilter());
        shiroFilter.setFilters(filterMap);

        // 拦截器
        Map<String, String> filterRuleMap = new LinkedHashMap<>();
        filterRuleMap.put("/login", "anon");
        filterRuleMap.put("/logout", "logout");
        filterRuleMap.put("/**", "jwt");
        shiroFilter.setFilterChainDefinitionMap(filterRuleMap);
        
        return shiroFilter;
    }
}
```

