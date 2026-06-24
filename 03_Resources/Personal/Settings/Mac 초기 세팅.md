### 생성
```shell
#!/bin/bash

# 1. Homebrew 설치
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Homebrew 경로 설정 (Apple Silicon 대응)
if [[ $(uname -m) == 'arm64' ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# 2. 애플리케이션 및 도구 설치
brew install --cask iterm2 intellij-idea docker slack
brew install git openjdk@21 hey zsh-syntax-highlighting

# 3. Git 설정
git config --global user.name "Duho Lee"
git config --global user.email "duholee@company.com"

# 4. Java 21 심볼릭 링크 (시스템 인식용)
sudo ln -sfn $(brew --prefix)/opt/openjdk@21/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-21.jdk

# 5. Oh My Zsh 설치 (비대화형 모드 --unattended)
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# 6. zsh-syntax-highlighting 설정 추가
echo "source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc

# 7. AWS CLI 설치
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
rm AWSCLIV2.pkg

# 8. 디렉토리 구조 생성
mkdir -p ~/Develop/Company ~/Develop/Personal ~/Develop/Scripts

# 9. alias 추가
add_alias() {
  local name=$1
  local value=$2
  
  if ! grep -q "alias $name=" ~/.zshrc; then
    echo "alias $name='$value'" >> ~/.zshrc
    echo "alias $name 추가 완료"
  else
    echo "이미 alias $name이(가) 존재합니다. 건너뜁니다."
  fi
}

alias com="cd ~/Develop/Company"
alias per="cd ~/Develop/Personal"
alias garden="cd ~/Develop/Personal/garden"
alias note="cd ~/Develop/Personal/manure"



echo "설치가 완료되었습니다. 터미널을 재시작해주세요!"
```


### 제거
```shell
#!/bin/bash

echo "⚠️ 개발 환경 삭제를 시작합니다..."

# 1. Homebrew로 설치한 패키지 및 Cask 삭제
echo "--- Homebrew 패키지 삭제 중 ---"
brew uninstall --cask iterm2 intellij-idea docker slack
brew uninstall git openjdk@21 hey zsh-syntax-highlighting

# 2. Java 심볼릭 링크 제거
echo "--- Java 설정 제거 중 ---"
sudo rm -f /Library/Java/JavaVirtualMachines/openjdk-21.jdk

# 3. AWS CLI 삭제
echo "--- AWS CLI 제거 중 ---"
sudo rm -rf /usr/local/aws-cli
sudo rm /usr/local/bin/aws
sudo rm /usr/local/bin/aws_completer
rm -rf ~/.aws

# 4. Oh My Zsh 및 관련 설정 삭제
echo "--- Oh My Zsh 및 Zsh 설정 제거 중 ---"
# zsh-syntax-highlighting 설정 한 줄만 삭제 (나머지 .zshrc는 보존하거나 아래에서 통째로 삭제)
sed -i '' '/zsh-syntax-highlighting/d' ~/.zshrc 2>/dev/null || true

# 만약 Oh My Zsh 자체를 아예 지우고 싶다면 아래 주석 해제
chmod +x ~/.oh-my-zsh/tools/uninstall.sh
~/.oh-my-zsh/tools/uninstall.sh --unattended
rm -rf ~/.oh-my-zsh ~/.zshrc

# 5. 생성했던 디렉토리 구조 삭제 (주의: 작업 중인 코드가 있다면 백업 필수!)
echo "--- 개발 디렉토리 제거 중 ---"
rm -rf ~/Develop  # <--- 진짜 다 지워도 되면 주석 해제하세요!

# 6. Homebrew 자체 삭제 (완전 초기화를 원할 경우)
echo "--- Homebrew 자체 삭제 중 ---"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"

echo "✅ 모든 환경이 정리되었습니다. 터미널을 재시작하세요."
```