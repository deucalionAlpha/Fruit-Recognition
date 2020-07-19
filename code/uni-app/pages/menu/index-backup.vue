<template>
	<view class="container">
		<view class="banner" id="banner">
			<swiper :autoplay="autoplay" :interval="interval" :circular="circular" class="swiper-box">
				<swiper-item v-for="(item,index) in banner" :key="index">
					<image :src="item" class="banner-image"></image>
				</swiper-item>
			</swiper>
		</view>
		<view class="page-body">
			<scroll-view class="nav-left" scroll-y :style="'height:'+height+'px'">
				<view class="nav-left-item" :key="index" :class="index==categoryActive?'active':''" v-for="(item,index) in shopList" @tap="categoryClick(index)">
					{{item.classify}}
				</view>
			</scroll-view>
			<scroll-view class="nav-right" scroll-y :scroll-top="scrollTop" @scroll="scroll" :style="'height:'+height+'px'" scroll-with-animation id="rightItem">
				<view :id="index===0?'first':''" class="nav-right-item" v-for="(item,index) in shopList" :key="index">
					<view class="item-header">{{item.classify}}</view>
					<view class="item-state" v-show="item.state !== ''">{{item.state}}</view>
					<view class="item-li" v-for="(shop,i) in item.data" :key="i">
						<image src="http://placehold.it/50x50" class="item-img"/>
						<view class="item-text">
							<view class="item-title">{{shop.title}}</view>
							<view class="item-en">{{shop.en}}</view>
							<view class="item-kind">默认：{{shop.kind}}</view>
							<view class="item-price">￥{{shop.price}}</view>
							<view class="plus-filled"><uni-icon type="plus-filled"></uni-icon></view>
						</view>
					</view>
				</view>
			</scroll-view>
		</view>
	</view>
</template>

<script>
	import uniIcon from "@/components/uni-icon.vue"
	export default {
		components: {
			uniIcon
		},
		data() {
			return {
				banner: [
					"https://s2.luckincoffeecdn.com/luckywebrm/images/pimg/about/contact.png",
					"https://s2.luckincoffeecdn.com/luckywebrm/images/pimg/about/model.png",
					"https://s2.luckincoffeecdn.com/luckywebrm/images/index/cooperation/part5_picture2.png",
				],
				indicatorDots: true,
				autoplay: false,
				circular: true,
				interval: 4000,
				duration: 500,
				storeOff: true,
				categoryList: [],
				subCategoryList: [],
				height: 0,
				categoryActive: 0,
				scrollTop: 0,
				scrollHeight: 0,
				itemHeight: 0,
				itemObj: [],
				itemTop: 0,
				shopList: [{
					classify : "人气Top",
					state: "",
					data: [{
						title: "圣诞姜饼人拿铁",
						en: "Christmas Gingerbread Latte",
						kind: "大/默认奶油/热",
						price: "27"
					},{
						title: "棒果拿铁",
						en: "Hazelnut Latte",
						kind: "大/单糖/热",
						price: "27"
					}]
				},{
					classify : "大师咖啡",
					state: "WBC（世界咖啡师大赛）冠军团队拼配",
					data: [{
						title: "拿铁",
						en: "Latte",
						kind: "大/无糖/热",
						price: "24"
					},{
						title: "香草拿铁",
						en: "Vanilla Latte",
						kind: "大/单糖/热",
						price: "27"
					},{
						title: "香草拿铁",
						en: "Vanilla Latte",
						kind: "大/单糖/热",
						price: "27"
					},{
						title: "香草拿铁",
						en: "Vanilla Latte",
						kind: "大/单糖/热",
						price: "27"
					},{
						title: "香草拿铁",
						en: "Vanilla Latte",
						kind: "大/单糖/热",
						price: "27"
					},{
						title: "香草拿铁",
						en: "Vanilla Latte",
						kind: "大/单糖/热",
						price: "27"
					}]
				},{
					classify : "零度拿铁",
					
					state: "不含咖啡的拿铁",
					data: [{
						title: "抹茶拿铁",
						en: "Latte",
						kind: "大/热",
						price: "27"
					},{
						title: "抹茶拿铁",
						en: "Latte",
						kind: "大/热",
						price: "27"
					},{
						title: "抹茶拿铁",
						en: "Latte",
						kind: "大/热",
						price: "27"
					},{
						title: "抹茶拿铁",
						en: "Latte",
						kind: "大/热",
						price: "27"
					},{
						title: "抹茶拿铁",
						en: "Latte",
						kind: "大/热",
						price: "27"
					},{
						title: "抹茶拿铁",
						en: "Latte",
						kind: "大/热",
						price: "27"
					},{
						title: "抹茶拿铁",
						en: "Latte",
						kind: "大/热",
						price: "27"
					}]
				}]
			}
		},
		methods: {
			scroll(e) {
				this.scrollHeight = e.detail.scrollHeight;
				var navrightItem = uni.createSelectorQuery().selectAll(".nav-right-item");
				this.itemTop = e.detail.scrollTop;
// 				uni.pageScrollTo({
// 					scrollTop: rects.top + res[1].scrollTop,
// 					duration: 300
// 			　	})
				navrightItem.fields({
					size: true,
					scrollOffset: true,
					dataset: true
				}, data => {
					this.itemObj = data;
				}).exec();
				if(this.itemObj !== []){
					// console.log(this.itemTop,this.itemObj[0].height)
// 					for(var i = 0; i<this.itemObj.length; i++){
// 						if(this.itemTop < this.itemObj[i].height){
// 							console.log(i)
// 						}
// 					}
				}
			},
			categoryClick(index) {
				this.categoryActive = index;
				// this.scrollTop = -this.scrollHeight * index;
				// console.log(this.scrollHeight,index)
			},
			getElSize(id) { //得到元素的size
				return new Promise((res, rej) => {
					uni.createSelectorQuery().select("#" + id).fields({
						size: true,
						scrollOffset: true
					}, (data) => {
						res(data);
					}).exec();
				})
			}
		},
		onLoad: function () {
			this.height = Math.floor(uni.getSystemInfoSync().windowHeight - 124);
			// #ifdef APP-PLUS
			this.height = Math.floor(uni.getSystemInfoSync().windowHeight - 180);
			// #endif
		}
	}
</script>

<style>
	.swiper-box{height: 124px;}
	.banner{position: relative;}
	.banner-image{width: 100%;}
	
	.page-body {display: flex;}
	.nav {display: flex;width: 100%;}
	.nav-left {width: 180upx;background-color: #f7f7f7;}
	.nav-left-item {height: 86upx;border-bottom: solid 1px #ececec;font-size: 28upx;display: flex;align-items: center;justify-content: center;color: #666;}
	.nav-left-item:last-child{border-bottom: none;}
	.active {color: #333;background-color: #fff;font-weight: 700;}
	.nav-right {width: 570upx;background-color: #fff;}
	.nav-right-item {width: 100%;font-size: 28upx;padding: 0 26upx;box-sizing: border-box;}
	.item-header{padding-top: 36upx;font-size: 24upx;font-weight: 700;line-height: 24upx;}
	.item-state,.item-en,.item-kind{font-size: 20upx;line-height: 20upx;color: #999;}
	.item-state{margin-top: 10upx;}
	.item-li{padding: 22upx 0;position: relative;border-bottom: 1px solid #f1f1f1;height: 134upx;}
	.nav-right-item .item-li:last-child{border-bottom: none;}
	.item-img{width: 134upx;height: 134upx;border-radius: 8upx;}
	.item-text{display: inline-block;vertical-align: top;margin-left: 16upx;}
	.item-title{font-size: 28upx;line-height: 28upx;font-weight: 700;}
	.item-en{margin: 10upx 0 8upx 0;}
	.item-price{font-size: 28upx;line-height: 28upx;font-weight: 700;margin-top: 28upx;}
	.plus-filled{position: absolute;bottom: 16upx;right: 0;color: #81aad2;}
	.fixed{position: fixed;top: 0;left: 206upx;background: #fff;}
</style>
