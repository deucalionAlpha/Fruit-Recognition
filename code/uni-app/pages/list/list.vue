<template>
	<view class="content">
			
			<view class="search-block">
			           <view class="search-ico-wapper">
			               <image src="../../static/search.png" class="search-ico" mode=""></image>
			           </view>
			            <input type="text" value="" placeholder="点击输入搜索内容" class="search-text" maxlength="15"/>
			            <view class="search-ico-wapper1">
			                <image src="../../static/go.png" class="search-ico-1" mode=""></image>
			            </view>
			       </view>
			
			<view class="uni-flex uni-row" style="background-color: #ffffff;margin: 20upx 20upx 20upx 20upx; border-radius: 30upx;" v-for="(item,index) in listObj":key="index" @tap="go(url='/pages/menu/index')">
				<view class="text uni-flex" style="width: 200rpx;height: 220rpx;-webkit-justify-content: center;justify-content: center;-webkit-align-items: center;align-items: center;">
					<image :src="item.imgurl" style="width: 150rpx;height: 150rpx;"></image>
				</view>
				<view class="uni-flex uni-column" style="-webkit-flex: 1;flex: 1;-webkit-justify-content: space-between;justify-content: space-between;">
					<view class="text"  style="height: 45rpx;text-align: left;padding-left: 20rpx;padding-top: 30rpx;" >
						{{item.liText}}
					</view>
					<view class="text"  style="color:#555555; font-size: 20upx; left;padding-left: 20rpx;padding-top: 10rpx;" >
						{{item.liEn}}
					</view>
					<view class="text"  style=" left;padding-left: 20rpx;padding-top: 10rpx;" >
						立即购买
					</view>
					<!--<view class="uni-flex uni-row" >
						<view class="text" style="-webkit-flex: 1;flex: 1;">立即购买</view>
					</view>-->
				</view>
			</view>

		
	</view>
</template>
<script>
	export default {
		data() {
			return {
				refreshing: false,
				loadMoreText: '加载中...',
				dataList: [],
				id: 0,
				fetchPageNum: 0,
				listObj: [
					{
						"liText": "世纪华联",
						"liEn": "苹果特价",
						"imgurl": "../../static/shop_1.jpg",
						"url": "/pages/menu/index"
					},
					{
						"liText": "人人家超市",
						"liEn": "新鲜水果，活动多多",
						"imgurl": "../../static/shop_2.jpg",
						"url": "/pages/mine/wallet/index"
					},
					{
						"liText": "云峰水果店",
						"liEn": "盒装水果，精致包装",
						"imgurl": "../../static/shop_3.jpg",
						"url": "/pages/home/presented"
					},
					{
						"liText": "永盛成超市",
						"liEn": "",
						"imgurl": "../../static/shop_4.jpg",
						"url": ""
					}
				],
			}
		},
		onLoad(e) {
			uni.setNavigationBarTitle({
				title: '专题：' + e.type
			});
			this.id = e.id;
			// 防止app里由于渲染导致转场动画卡顿
			setTimeout(() => {
				this.getData();
			}, 300);
			uni.getProvider({
				service: 'share',
				success: (e) => {
					let data = [];
					for (let i = 0; i < e.provider.length; i++) {
						switch (e.provider[i]) {
							case 'weixin':
								data.push({
									name: '分享到微信好友',
									id: 'weixin'
								});
								data.push({
									name: '分享到微信朋友圈',
									id: 'weixin',
									type: 'WXSenceTimeline'
								});
								break;
							case 'qq':
								data.push({
									name: '分享到QQ',
									id: 'qq'
								});
								break;
							default:
								break;
						}
					}
					this.providerList = data;
				},
				fail: (e) => {
					console.log('获取分享通道失败', e);
				}
			});
		},
		onPullDownRefresh() {
			console.log('下拉刷新');
			this.refreshing = true;
			this.getData();
		},
		onReachBottom() {
			console.log('上拉加载刷新');
			if (this.fetchPageNum > 4) {
				this.loadMoreText = '没有更多了'
				return;
			}
			this.getData();
		},
		methods: {
			
			go(url){
				if(url == '/pages/menu/index'){
					uni.navigateTo({
						url: url
					})
				}else{
					uni.navigateTo({
						url: url
					})
				}
			},
			
			getData(e) {
				uni.request({
					url: this.$serverUrl + '/api/picture/list.php?type=' + this.id,
					success: (ret) => {
						if (ret.statusCode !== 200) {
							console.log('请求失败', ret)
							return;
						}

						const data = ret.data.data;

						if (this.refreshing && data[0].id === this.dataList[0].id) {
							uni.showToast({
								title: '已经最新',
								icon: 'none',
							});
							this.refreshing = false;
							uni.stopPullDownRefresh();
							return;
						}

						let list = [];
						for (var i = 0; i < data.length; i++) {
							var item = data[i];
							item.guid = this.newGuid() + item.id
							list.push(item);
						}

						if (this.refreshing) {
							this.refreshing = false;
							uni.stopPullDownRefresh();
							this.dataList = list;
							this.fetchPageNum = 2;
						} else {
							this.dataList = this.dataList.concat(list);
							this.fetchPageNum += 1;
						}
						this.fetchPageNum += 1;
					}
				});
			},
			newGuid() {
				let s4 = function() {
					return (65536 * (1 + Math.random()) | 0).toString(16).substring(1);
				}
				return (s4() + s4() + "-" + s4() + "-4" + s4().substr(0, 3) + "-" + s4() + "-" + s4() + s4() + s4()).toUpperCase();
			},
			goDetail(e) {
				uni.navigateTo({
					url: '/pages/detail/detail?data=' + encodeURIComponent(JSON.stringify(e))
				});
			},
			share(e) {
				if (this.providerList.length === 0) {
					uni.showModal({
						title: '当前环境无分享渠道!',
						showCancel: false
					});
					return;
				}
				let itemList = this.providerList.map(function(value) {
					return value.name;
				});
				uni.showActionSheet({
					itemList: itemList,
					success: (res) => {
						uni.share({
							provider: this.providerList[res.tapIndex].id,
							scene: this.providerList[res.tapIndex].type && this.providerList[res.tapIndex].type === 'WXSenceTimeline' ?
								'WXSenceTimeline' : 'WXSceneSession',
							type: 0,
							title: 'uni-app模版',
							summary: e.title,
							imageUrl: e.img_src,
							href: 'https://uniapp.dcloud.io',
							success: (res) => {
								console.log('success:' + JSON.stringify(res));
							},
							fail: (e) => {
								uni.showModal({
									content: e.errMsg,
									showCancel: false
								});
							}
						});
					}
				});
			}
		}
	}
</script>

<style>
	.search-ico, .search-ico-1{
		     width: 40upx;
		     height: 40upx;
		 }
		
		.search-block{
		     display: flex;
		     flex-direction: row;
		     padding-left: 5upx;
		     position: relative;
		     top: 10upx;
			 
		 }
		 
		 .search-text{
		      font-size: 14px;
		      background-color: #FFFFFF;
		      height: 60upx;
		      width: 530upx;
		  }
		  
		  .search-ico-wapper{
		       background-color: #FFFFFF;
		       display: flex;
		       flex-direction:column;
		       justify-content: center;
		       padding: 0upx 0upx 0upx 40upx;
		       border-bottom-left-radius:18px;
		       border-top-left-radius: 18px;
		   }
		   .search-ico-wapper1{
		       background-color: #FFFFFF;
		       display: flex;
		       flex-direction:column;
		       justify-content: center;
		       padding: 0upx 40upx 0upx 0upx;
		       border-bottom-right-radius:18px;
		       border-top-right-radius: 18px;
		   }
		   
		   .content{padding: 0 24upx;border-top: 1px solid #e7e7e7;}
		
		.try {
			flex: 1;
			width: 710upx;
			margin: 20upx;
			flex-direction: row;
			flex-wrap: wrap;
			justify-content: flex-start;
			align-content: flex-start;
		}
		.swiper-box{height: 421upx;}
		.banner{position: relative;}
		.banner-image{width: 100%;}
		.scan{position: absolute;top: 48upx;right: 30upx;width: 80upx;height: 80upx;color: #fff;background: rgba(0,0,0,0.6);line-height: 74upx;text-align: center;border-radius: 50%;padding-top: 10upx;box-sizing: border-box;}
		.store,.list{background: #fff;}
		.store{height: 136upx;padding: 36upx 40upx 0 40upx;box-sizing: border-box;position: relative;}
		.store-off{position: absolute;top: 50%;right: 40upx;width: 182upx;height: 66upx;line-height: 66upx;text-align: center;border: 1px solid #5d92c7;border-radius: 40upx;color: #5d92c7;margin-top: -33upx;padding: 1px;font-size: 24upx;}
		.store-btn{display: inline-block;width: 50%;line-height: 66upx;}
		.store-btn.active{color: #fff;background-color: #7ca7d2;border-radius: 40upx;}
		.store-text,.list-text{line-height: 28upx;font-size: 32upx;}
		.store-distance,.list-en{font-size: 18upx;color: #5e5e5e;line-height: 18upx;margin-top: 23upx;}
		.list{padding: 0 40upx;}
		.list-cell{height: 118upx;border-top: 1px solid #efefef;position: relative;}
		.list-text{margin-top: 27upx;display: inline-block;}
		.list-right{position: absolute;top: 50%;right: 50upx;width: 76upx;height: 76upx;line-height: 76upx;text-align: center;border-radius: 50%;border: 1px solid #c6baad;margin-top: -38upx;color: #784f2d;}
		.list-en{font-size: 16upx;}
		.list-img{width: 48upx;height: 48upx;margin-top: 12upx;}
		.list-hint{font-size: 16upx;color: #fff;background-color: #e06e11;padding: 0 4upx;border-radius: 3px;line-height: 24upx;display: inline-block;vertical-align: top;}

</style>
