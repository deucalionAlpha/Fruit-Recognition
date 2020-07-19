<template>
	<view class="content">
		<view class="banner">
			<swiper :autoplay="autoplay" :indicator-dots="indicatorDots" :interval="interval" :circular="circular" class="swiper-box">
				<swiper-item v-for="(item,index) in banner" :key="index">
					<image :src="item" class="banner-image"></image>
				</swiper-item>
			</swiper>
		</view>
		
			
			
		<view class="uni-flex uni-row" style="background-color: #ffffff;">
				
			<image src="../../static/detail.jpg" style="height: 3300upx; width: 750upx;"></image>
				
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
					"../../static/new_1.jpg",
					"../../static/new_2.jpg",
					"../../static/new_3.jpg",
					"../../static/new_4.jpg",
				],
				indicatorDots: true,
				autoplay: true,
				circular: true,
				interval: 2000,
				duration: 500.,
				storeOff: true,
				

				
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

		}
	}

</script>

<style>
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
