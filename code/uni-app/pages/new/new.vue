<template>
	<view class="index">

		<view class="search-block">
		           <view class="search-ico-wapper">
		               <image src="../../static/search.png" class="search-ico" mode=""></image>
		           </view>
		            <input type="text" value="" placeholder="点击输入搜索内容" class="search-text" maxlength="15"/>
		            <view class="search-ico-wapper1">
		                <image src="../../static/go.png" class="search-ico-1" mode=""></image>
		            </view>
		       </view>
		
		<view class="grid">
			
			
		
			<view class="grid-c-06" v-for="(item,index) in lists" :key="index">
				<view class="panel" @click="goDetail(item)">
					<image class="card-img card-list2-img" :src="item.imgurl"></image>
					<text class="card-num-view card-list2-num-view">{{item.img_num}}P</text>
					<view class="card-bottm row" style="display: flex;">
						<view class="car-title-view row" >
							<text class="card-title card-list2-title">{{item.title}}</text>	
						</view>
					<view @click.stop="share(item)" class="card-share-view"></view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				refreshing: false,
				fetchPageNum: 1,
				lists:[
					{
						"title": "柚子皮除异味",
						"imgurl": "../../static/new_1.jpg",
						"img_num":"4",
					},
					{
						"title": "越吃越瘦的水果",
						"imgurl": "../../static/new_7.jpg",
						"img_num":"4",
					},
					{
						"title": "柚子皮养生用法",
						"imgurl": "../../static/new_2.jpg",
						"img_num":"4",
					},
					{
						"title": "石榴的作用",
						"imgurl": "../../static/new_3.jpg",
						"img_num":"4",
					},
					{
						"title": "水果应该这样吃",
						"imgurl": "../../static/new_6.jpg",
						"img_num":"4",
					},
					{
						"title": "石榴的益处",
						"imgurl": "../../static/new_4.jpg",
						"img_num":"4",
					},
					{
						"title": "什么季节吃什么水果",
						"imgurl": "../../static/new_5.jpg",
						"img_num":"4",
					},
					{
						"title": "水果的挑选办法",
						"imgurl": "../../static/new_8.jpg",
						"img_num":"4",
					},
				],
			}
		},
		onLoad() {
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
					console.log('获取登录通道失败', e);
				}
			});
		},

		onReachBottom() {
			this.getData();
		},
		methods: {
			goDetail(e) {
				uni.navigateTo({
					url: '../detail/detail'
				})
			},
			share(e) {
				if (this.providerList.length === 0) {
					uni.showModal({
						title: '当前环境无分享渠道!',
						showCancel: false
					})
					return;
				}
				let itemList = this.providerList.map(function(value) {
					return value.name
				})
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
								})
							}
						});
					}
				})
			}
		}
	}
</script>

<style>
	.grid{
		padding-top: 10px;
	}
	
	.search-ico, .search-ico-1{
	     width: 40upx;
	     height: 40upx;
	 }
	
	.search-block{
	     display: flex;
	     flex-direction: row;
	     padding-left: 30upx;
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
</style>
