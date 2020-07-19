<template>
	<view class="content" >
		
		<view class="banner">
			<swiper :autoplay="autoplay" :indicator-dots="indicatorDots" :interval="interval" :circular="circular" class="swiper-box">
				<swiper-item v-for="(item,index) in banner" :key="index">
					<image :src="item" class="banner-image"></image>
				</swiper-item>
			</swiper>
			<view class="scan" @tap="scanCode">
				<uni-icon type="search"></uni-icon>
			</view>
		</view>
		
			<view class="tags" style="display: flex;">
				<block v-for="value in data" :key="value.key">
					<view class="tag" @tap="goList(value)">
						<image class="tag-img" :src="value.icon"></image>
						<text class="tag-text">{{value.type}}</text>
					</view>
				</block>
			</view>
			
			<view class="search-block">
			           <view class="search-ico-wapper">
			               <image src="../../static/search.png" class="search-ico" mode=""></image>
			           </view>
			            <input type="text" value="" placeholder="点击输入搜索内容" class="search-text" maxlength="15"/>
			            <view class="search-ico-wapper1">
			                <image src="../../static/go.png" class="search-ico-1" mode=""></image>
			            </view>
			       </view>
			
			<view class="uni-flex uni-row" style="background-color: #ffffff; margin: 20upx 20upx 20upx 20upx; border-radius: 30upx;" v-for="(item,index) in listObj":key="index" @tap="go(url='/pages/menu/index')">
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
					<view class="text"  style=" left;padding-left: 20rpx;padding-top: 0rpx;" >
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
	import uniIcon from "../uni-icon.vue"
	export default {
		components: {
			uniIcon
		},
		data() {
			return {
				banner: [
					"../../static/banner_1.jpg",
					"../../static/banner_2.jpg",
					"../../static/banner_3.jpg",
				],
				indicatorDots: true,
				autoplay: true,
				circular: true,
				interval: 2000,
				duration: 500.,
				storeOff: true,
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
				
				data: [{
						type: '苹果',
						id: 1,
						key: 1,
						icon: '../../static/apple.png'
					},
					{
						type: '香蕉',
						id: 2,
						key: 2,
						icon: '../../static/banana.png'
					},
					{
						type: '橙子',
						id: 3,
						key: 3,
						icon: '../../static/cheng.png'
					},
					{
						type: '其他',
						id: 4,
						key: 4,
						icon: '../../static/other.png'
					},
					],

				
			}
		},

		methods: {
			goList(value) {
				uni.navigateTo({
					url: '../list/list?type=' + value.type + '&id=' + value.id
				})
			},
			store() {
				this.storeOff = !this.storeOff;
			},
			scanCode: function () {
				var that = this
				uni.scanCode({
					success: function (res) {
						that.result = res.result
					},
					fail: function (res) {}
				})
			},
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
	     padding-left: 30upx;
	     position: relative;
	     top: -40upx;
		 
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
