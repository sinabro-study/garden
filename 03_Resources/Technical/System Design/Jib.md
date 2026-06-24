## Jib란?
- Dockerfile없이 Java Application을 컨테이너 이미지로 빌드하는 도구

![[Screenshot 2026-01-23 at 9.06.19 PM.png]]

```
# 일반 프로세스
코드 변경 -> Jar 생성 -> Docker Build -> 이미지 생성

# Jib 프로세스
코드 변경 -> 이미지 생성
```


## 적용 방법
```gradle
plugin {
  id 'com.google.cloud.tools.jib' version '3.4.3'
}

jib {
  def env = project.properties["env"] ?: "dev"
  def service = "#{service_name}"
  
  from {
    image = 'amazoncorreto:#{version}'
  }
  to {
    image = '#{aws_account_id}.dkr.ecr.{region}.amazonaws.com/$env-$service'
    project.afterEvaluate {
      tag = ["latest", getGitHash()]
    }
  }
}

def getGitHash() {
  def stdOut = new ByteArrayOutputStream()
  exec {
    commandLine 'git', 'rev-parse', '--short', 'HEAD'
    standardOutput = stdOut
  }
  
  return stdOut.toString().trim()
}

tasks {
  task downloadAgent(type: Download) {
    src '#{datadog_s3_url}'
    dest 'src/main/jib/agents/dd-java-agent.jar'
  }
}

tasks.jib {
  dependsOn("downloadAgent")
}
```

```bash
sudo yum install docker -y
aws ecr get-login-password --region ap-northeast-2 | docker login --username     AWS --password-stdin ${aws_account_id}.dkr.ecr.{region}.amazonaws.com

./gradlew jib
```
