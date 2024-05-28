
let $ = function (str) { return document.querySelector(str) }
// window.onload = function(){
let url = document.querySelector('link').href
let styleDom = document.createElement('style')
styleDom.type = 'text/css'
document.documentElement.appendChild(styleDom)

// 上升下降控制
function lineChartControl(){
  let $2 = function (str) { return document.querySelector(str) }
  let mouthArray = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
  let iosData = window.injectedSwiftString || '2023-04-08,65.1,70.2,kg,5 week'
  iosData = iosData.split(',')
  let timeDate = new Date(iosData[0])
  $2('.head-time').innerHTML = iosData[4];
  for(let dom of  document.querySelectorAll('.last-time')){
  	dom.innerHTML = `${mouthArray[timeDate.getMonth()]} ${timeDate.getDate()}`
  }
  for(let dom of  document.querySelectorAll('.today-kg')){
  	dom.innerHTML = iosData[1] + iosData[3]
  }
  for(let dom of  document.querySelectorAll('.last-kg')){
  	dom.innerHTML = iosData[2] + ' ' + iosData[3]
  }
  let difference = 0
  difference = Math.abs(parseFloat(iosData[1]) - parseFloat(iosData[2]));
  for(let dom of  document.querySelectorAll('.difference')){
  	dom.innerText = parseInt(difference*10)/10 + iosData[3]
  }
  $2('.down-model').style.display = 'none'
  $2('.flat-model').style.display = 'none'
  $2('.rise-model').style.display = 'none'
  //下降
  if(difference > 0){
    $2('.down-model').style.display = 'block'
  }
   //持平
  if(difference == 0){
    $2('.flat-model').style.display = 'block'
  }
   //上升
  if(difference < 0){
    $2('.rise-model').style.display = 'block'
  }
}

function showSmallPopup() {
  let maskCon = document.querySelector('.mask-con');
  maskCon.style.zIndex = '4';
  maskCon.style.opacity = '1';
  document.querySelector('.popup-con').style.transform = 'scale(1)';
}
function closePopup() {
  document.querySelector('.popup-con').style.transform = 'scale(0.7)'
  document.querySelector('.mask-con').style.opacity = '0'
  setTimeout(() => {
    document.querySelector('.mask-con').style.zIndex = '2'
  }, 200)
}

//倒计时
let centerTime = document.querySelector('.time-center')
let endTimeDom = document.querySelector('.time-end')
let minuts = 59, seconds = 59;
HTMLDivElement.prototype.setValue = function (value) { this.innerHTML = value }
function updateTime() {
  let minutsShowTime = minuts
  let secondsShowTime = seconds
  if (minuts < 10) { minutsShowTime = `0${minuts}` }
  if (seconds < 10) { secondsShowTime = `0${seconds}` }
  centerTime.setValue(minutsShowTime)
  endTimeDom.setValue(secondsShowTime)
}
updateTime()
function reduceTime() {
  let timer = setInterval(() => {
    // 时间修改
    seconds = seconds - 1
    if (seconds === -1) {
      seconds = 59
      minuts = minuts - 1
      if (minuts === 0) {
        clearInterval(timer)
      }
    }
    updateTime()
  }, 1000)
}
// 执行
coverImage()
// addCutFunction()
reduceTime()
// 用于页面初始化
function web_reload() {
  // 页面初始化
  addCutFunction()
  // 时间初始化
  minuts = 59, seconds = 59;
}
//背景图片加载完成后进行替换
function coverImage() {
  let clsoeBtns = [...document.querySelectorAll('.close-btn-main')];
  let clsoeBtn = document.querySelector('.close-btn-main');
  let clsoeText = document.querySelector('.close-btn-text');
  let videoFather = document.querySelector('.video-father')
  let video = document.createElement('video')
  video.classList.add('bg-video')
  videoFather.appendChild(video)
  // 默认 ix 比例的视频作为默认
  let videoSrc = 'https://aloy.7mfitness.com/cms/videoClass/video/859d53a91cf54d05b6e486830ba311fb.mp4?alt=media&name=104_ob_video.mp4'
  /**
  let ratio = Math.round(document.documentElement.clientWidth/document.documentElement.clientHeight * 100)/100
  // x 的比例0.46, 8 的比列0.56 ，ipad 比例 0.75
  if( ratio == 0.56 ){
    videoSrc = ''
  }
  if( ratio == 0.75 ){
    videoSrc = ''
  }
  **/
  video.src = videoSrc
  video.setAttribute("playsinline", '')
  video.setAttribute("webkit-playsinline", '')
  video.addEventListener('ended', () => {
    try {
      clsoeBtns[1].click()
      swiftCallback('playEnded')
    }
    catch (error) {
      console.log(error)
    }
  })
  let tab1 = $('.tab-1'), tab2 = $('.tab-2');
  $('#btn-to-page2').addEventListener('click', function () {
    tab1.style.transform = "translate(-100%, 0)"
  })
  $('#btn-to-page3').addEventListener('click', function () {
    tab2.style.transform = "translate(-100%, 0)"
    showSmallPopup()
  })
  let page1 = document.querySelector('.page-1')
  let page2 = document.querySelector('.page-2')
  let page3 = document.querySelector('.page-3')
  clsoeBtns.some((closeDom, index) => {
    closeDom.addEventListener("click", () => {
      if (index === 0) {
        page1.style.transform = "translate(0px, 100%)"
        video.play()
      }
      if (index === 1) {
        page2.style.transform = "translate(0px, 100%)"
        video.pause()
      }
    })
  })
  
  let closeUrlAll = 'url("https://assets-global.website-files.com/64cb62b0f407f54e3b5804f3/64ec008b35fe83d6a05fd1a8_%E5%BA%95%E8%89%B2%403x%20(4).png")'
  let closeUrl = closeUrlAll.match(/url\("([^]{0,})"\)/)[1]

  console.log('执行了一次全局js代码')
  // bgImage.style.backgroundImage = 'none'
  // bgImage.style.background = 'linear-gradient(to bottom,rgb(198,196,241) 1%,white)'
  // let urlArray = [closeUrl, bgImageUrl]
  let urlArray = [closeUrl]
  console.log(closeUrl)
  let urlLoadCount = 0
  // close btn 按钮替换
  window.onpageshow = function () {
    document.querySelector('#mask-close-btn').addEventListener('click', closePopup)
    for (let url of urlArray) {
      let img = document.createElement('img')
      img.src = url
      img.style.display = 'none'
      document.documentElement.appendChild(img)
      img.onload = () => {
        urlLoadCount += 1
        // 所需图片都加载完成
        if (urlLoadCount === urlArray.length) {
          // bgImage.style.background = bgImageBackground
          // 新增关闭文字 2023-1-11 16.01
          clsoeBtns.some(clsoeBtn => {
            clsoeBtn.style.backgroundImage = closeUrlAll
            clsoeBtn.style.backgroundSize = 'cover'
            clsoeBtn.style.color = 'rgba(0,0,0,0)'
          })
        }
      }
    }
  }
}
function pageShow() {
  setTimeout(() => { swiftCallback("duolingoInro1Show") }, 100)
}
// 给按钮添加切换功能
function addCutFunction() {
  HTMLElement.prototype.noShow = function () {
    this.style.display = 'none'
  }
  HTMLElement.prototype.show = function () {
    this.style.display = 'flex'
  }
  //先获取被控制的三个page dom
  let page1 = $('.tab-1'), page2 = $('.tab-2'), page3 = $('.tab-3');
  // 控制开始只展示第一页
  page1.show();
  page2.noShow();
  page3.noShow();
  $('#btn-to-page2').addEventListener('click', function () {
    page1.noShow();
    page2.show();
    page3.noShow();
    (window.swiftCallback && swiftCallback("duolingoInro2Show"))
  })
  $('#btn-to-page3').addEventListener('click', function () {
    page1.noShow();
    page2.noShow();
    page3.show();
    setTimeout(showSmallPopup, 200);
    (window.swiftCallback && swiftCallback("duolingoPaywallShow"))
  })
}