var utils = require('../../utils/util.js');
var log = require('../../utils/log.js');
//var seqId = util.wxuuid();
const app = getApp();
//引入插件：微信同声传译
const plugin = requirePlugin('WechatSI');
//获取全局唯一的语音识别管理器recordRecoManager
const manager = plugin.getRecordRecognitionManager();

Page({

  /**
   * 页面的初始数据
   */
  data: {
    //语音
    recordState: false, //录音状态
    content: '',//内容
    choices:["C++","C","Python"],
    choiceIndex:0
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    //识别语音
    this.initRecord();
  },
  // 手动输入内容
  conInput: function (e) {
    this.setData({
      content: e.detail.value,
    })
    console.log(this.data.content)
  },
  //识别语音 -- 初始化
  initRecord: function () {
    const that = this;
    // 有新的识别内容返回，则会调用此事件
    manager.onRecognize = function (res) {
      console.log(res)
    }
    // 正常开始录音识别时会调用此事件
    manager.onStart = function (res) {
      console.log("成功开始录音识别", res)
    }
    // 识别错误事件
    manager.onError = function (res) {
      console.error("error msg", res)
    }
    //识别结束事件
    manager.onStop = function (res) {
      console.log('..............结束录音')
      console.log('录音临时文件地址 -->' + res.tempFilePath);
      console.log('录音总时长 -->' + res.duration + 'ms');
      console.log('文件大小 --> ' + res.fileSize + 'B');
      console.log('语音内容 --> ' + res.result);
      if (res.result == '') {
        wx.showModal({
          title: '提示',
          content: '听不清楚，请重新说一遍！',
          showCancel: false,
          success: function (res) { }
        })
        return;
      }
      var text = that.data.content + res.result;
      that.setData({
        content: text
      })
    }
  },
  //语音  --按住说话
  touchStart: function (e) {
    this.setData({
      recordState: true  //录音状态
    })
    // 语音开始识别
    manager.start({
      lang: 'zh_CN',// 识别的语言，目前支持zh_CN en_US zh_HK sichuanhua
    })
  },
  //语音  --松开结束
  touchEnd: function (e) {
    this.setData({
      recordState: false
    })
    // 语音结束识别
    manager.stop();
  },

  bindCasPickerChange: function (e) {
    console.log('用户选的是', this.data.choices[e.detail.value])
    this.setData({
      choiceIndex: e.detail.value
    })
  },
  send: function () {

    var flag = this

    if (this.data.content.trim() == "") {

      wx.showToast({

        title: '消息不能为空哦~',

        icon: "none",

        duration: 2000

      })

    }
    else {
      wx.showLoading({
        title: '正在转换',

      })
      wx.request({
        url: 'https://' + app.globalData.rotBackIp + ':' + app.globalData.rotBackPort + '/dataSend',
        data: {
          seqId: utils.wxuuid(),
          openId: app.globalData.openid,
          message: this.data.content,
          language: 'python'
        },
        method: 'POST',
        header: {
          'content-type': 'application/json' // 默认值
        },
        success(res) {
          wx.hideLoading();
          console.log("send " + ", 返回:")
          console.log(res.data)
          var ret_code = res.data.ret_code
          var ret_info = res.data.info
          if (ret_code == 1) {
            wx.showModal({
              title: '执行成功',
              content: ret_info,
              showCancel: false
            })
            flag.setData({
              codeContent: res.data.text
            })
          }
          else {
            wx.showModal({
              title: '执行失败',
              content: ret_info,
              showCancel: false
            })
          }
          
        },
        fail(res) {
          wx.hideLoading();
          wx.showModal({
            title: '错误提示',
            content: '服务器未响应，请稍候再试',
            showCancel: false,
            success(res) {
              if (res.confirm) {
                // wang 此段需要恢复
                log.error('服务器发生错误！')
               
              }
            }
          })
        }
      })
  }
  }
})