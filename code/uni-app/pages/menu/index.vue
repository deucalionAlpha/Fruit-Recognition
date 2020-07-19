<template>
	<view class="container">
		<!-- <view class="banner" id="banner">
			<swiper :autoplay="autoplay" :interval="interval" :circular="circular" class="swiper-box">
				<swiper-item v-for="(item,index) in banner" :key="index">
					<image :src="item" class="banner-image"></image>
				</swiper-item>
			</swiper>
		</view> -->
		<view class="page-body">
			<scroll-view class="nav-left" scroll-y :style="'height:'+height+'px'">
				<view class="nav-left-item" :class="index==categoryActive?'active':''" v-for="(item,index) in shopList" :key="index" @tap="categoryClick(index)">{{item.classify}}</view>
			</scroll-view>
			<scroll-view class="nav-right" scroll-y :scroll-top="scrollTop" @scroll="scroll" :style="'height:'+height+'px'" scroll-with-animation id="rightItem">
				<view class="nav-right-item">
					<view class="item-header">{{itemObj.classify}}</view>
					<view class="item-state" v-show="itemObj.state !== ''">{{itemObj.state}}</view>
					<view class="item-li" v-for="(shop,i) in itemObj.shopData" :key="i"  @tap="showMiddlePopup(shop,i)">
						<image :src="shop.imgurl" class="item-img"/>
						<view class="item-text">
							<view class="item-title">{{shop.title}}</view>
							<view class="item-en">{{shop.en}}</view>
							<view class="item-default">默认：
								<text v-for="d in shop.default" :key="d">{{d}} </text>
							</view>
							<view class="item-price">￥{{shop.price}}</view>
							<view class="plus-filled" stop><uni-icon type="plus-filled"></uni-icon></view>
						</view>
					</view>
				</view>
			</scroll-view>
		</view>
		<!-- <popup :show="showPopup" @hidePopup="hidePopup" @addTocart="addTocart" :popupData="popupData"></popup> -->
		<view v-show="showPopup">
			<view class="mask" v-show="showPopup" @tap="hidePopup"></view>
			<view class="popup" v-show="showPopup">
				<view class="popup-header">
					<view class="uni-icon uni-icon-close popup-close" @click="hidePopup"></view>
					<view class="popup-title">{{popupData.title}}</view>
					<view class="popup-en">{{popupData.en}}</view>
				</view>
				<view class="popup-middle">
					<view class="sort" v-for="(item,index) in popupData.kind" :key="index">
						<view class="sort-label">{{item.name}}</view>
						<view class="sort-select" :class="[item.selected == i ? 'active' : '']" v-for="(t,i) in item.type" :key="i" @tap="changeTab(index,i,item)">{{t}}</view>
					</view>
					<view class="describe">
						<view class="describe-title">商品描述</view>
						<view class="describe-text">
							本店精心打包新鲜水果，只为给顾客更好的体验
						</view>
					</view>
				</view>
				<view class="popup-footer">
					<view class="popup-price">
						<view>
							<view class="text-main">￥{{popupData.price}}</view>
							<view class="text-small">{{popupData.title}}￥{{popupData.price}}</view>
						</view>
						<view class="numbox">
							<view class="numbox-minus uni-icon uni-icon-minus" @tap="minus"></view>
							<view class="numbox-value">{{num}}</view>
							<view class="numbox-plus uni-icon uni-icon-plus-filled" @tap="plus"></view>
						</view>
					</view>
					<view class="btn-group">
						<button class="btn two-btn">收藏口味</button>
						<button class="btn three-btn" @tap="addTocart(popupData.id)">加入购物车</button>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import {
		mapState,
		mapMutations
	} from 'vuex'
	import uniIcon from "../uni-icon.vue"
	// import popup from "@/components/popup.vue"
	import shopData from "./data.json"
	
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
				popType: 'middle',
				showPopup: false,
				popupData: {},
				shopList: [],
				num: 1
			}
		},
		computed: {
			...mapState(['cartList'])
		},
		onLoad: function () {
			this.shopList = shopData.data;
// 			this.height = Math.floor(uni.getSystemInfoSync().windowHeight - 124);
// 			// #ifdef APP-PLUS
// 			this.height = Math.floor(uni.getSystemInfoSync().windowHeight - 180);
// 			// #endif
			this.height = Math.floor(uni.getSystemInfoSync().windowHeight);
			// #ifdef APP-PLUS
			this.height = Math.floor(uni.getSystemInfoSync().windowHeight - 56);
			// #endif
			this.itemObj = this.shopList[0];
		},
		methods: {
			...mapMutations(['calcTotal']),
			categoryClick(index) {
				this.categoryActive = index;
				this.itemObj = this.shopList[index];
			},
			hidePopup() {
				this.showPopup = false;
			},
			showMiddlePopup(item,i) {
				this.num = 1;
				this.popupData = this.itemObj.shopData[i];
				this.showPopup = true;
			},
			addTocart (id){
				var kind = this.popupData.kind;
				var type = "";
				var d = {
					id: id,
					title: this.popupData.title,
					price: this.popupData.price,
					num: this.num,
					type: "",
					isChecked: true
				}
				for(var i = 0;i<kind.length; i++){
					var s = kind[i].selected;
					if(i>0){
						d.type += '/' + kind[i].type[s]
					}else{
						d.type += kind[i].type[s]
					}
				}
				var cartList = this.cartList;
				var flag = true;
				if(cartList.length >= 1){
					for(var i = 0; i < cartList.length; i++){
						if(d.id == cartList[i].id && d.type == cartList[i].type){
							cartList[i].num = cartList[i].num + d.num;
							flag = false;
						}
					}
				}
				flag ? cartList.push(d) : "";
				this.calcTotal(cartList);
				this.showPopup = false;
			},
			changeTab(index,i,item) {
				this.popupData.kind[index].selected = i;
			},
			minus() {
				if(this.num > 1){
					this.num --;
				}else{
					this.num = 1;
				}
			},
			plus() {
				this.num ++;
			}
		}
	}
</script>

<style>
	.container{border-top: 1px solid #f0f0f0;}
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
	.item-state,.item-en,.item-default{font-size: 20upx;line-height: 20upx;color: #999;}
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
	
	
	.mask {position: fixed;z-index: 99;top: 0;right: 0;bottom: 0;left: 0;background-color: rgba(0, 0, 0, .3);}
	.popup {position: fixed;z-index: 999;background-color: #fff;box-shadow: 0 0 30upx rgba(0, 0, 0, .1);display: flex;flex-direction: column;
align-items: center;width: 690upx;height: 920upx;border-radius: 10upx;top: 50%;left: 50%;transform: translate(-50%, -50%);box-sizing: border-box;overflow: hidden;}
	.popup-header,.popup-middle,.popup-footer{width: 100%;}
	.popup-header{height: 288upx;position: relative;background: url(https://s2.luckincoffeecdn.com/luckywebrm/images/index/cooperation/part5_picture2.png) center;}
	.popup-title,.popup-en{color: #fff;margin-left: 20upx;vertical-align: bottom;}
	.popup-title{font-size: 34upx;line-height: 54upx;margin-top: 190upx;}
	.popup-en{font-size: 20upx;line-height: 20upx;}
	.popup-close{color: #fff;font-size: 56upx;position: absolute;top: 20upx;right: 20upx;}
	.popup-middle{height: 400upx;box-sizing: border-box;padding: 10upx 30upx 0;overflow: auto;}
	.popup-footer{height: 232upx;border-top: 1px solid #f1f1f1;}
	.popup-price{display: flex;justify-content: space-between;padding: 32upx 28upx 24upx 38upx;height: 120upx;box-sizing: border-box;border-bottom: 1px solid #f1f1f1;}
	.text-main{font-size: 32upx;line-height: 32upx;color: #222;margin-bottom: 15upx;}
	.text-small{font-size: 20upx;color: #333;line-height: 20upx;}
	.numbox{display: flex;}
	.numbox-minus,.numbox-plus{font-size: 56upx;line-height: 68upx;}
	.numbox-minus{color: #91b5d9;background-color: #fff;}
	.numbox-value{line-height: 68upx;margin: 0 16upx;color: #91b5d9;font-weight: 700;min-width: 20upx;}
	.numbox-plus{color: #fff;color: #91b5d9;}
	.btn-group{display: flex;justify-content: flex-end;margin-top: 26upx;}
	.btn{height: 60upx;line-height: 58upx;padding: 0;margin: 0;font-size: 24upx;text-align: center;color: #fff;border-radius: 0;margin-right: 14upx;}
	.first-btn{width: 206upx;border: 1px solid #dc5a00;background-color: #e06e11;}
	.two-btn{width: 170upx;border: 1px solid #6c9ccd;background-color: #f3f3f3;color: #73a1cf;}
	.three-btn{width: 180upx;border: 1px solid #6c9ccd;background-color: #7ca7d2;}
	.btn:after{border: none;}
	.sort{display: flex;margin-top: 30upx;}
	.sort-label{width: 120upx;line-height: 52upx;}
	.sort-select{width: 120upx;height: 50upx;text-align: center;border-radius: 30upx;border: 1px solid #e3dbd3;color: #e3dbd3;font-size: 24upx;line-height: 50upx;margin-right: 15upx;}
	.sort-select.active{background-color: #e3dbd3;color: #fff;font-weight: 400;}
	.describe{border-top: 1px solid #f1f1f1;margin-top: 30upx;padding: 30upx 0 10upx;}
	.describe-title{margin-bottom: 10upx;}
	.describe-text{color: #666;font-size: 24upx;}
</style>
