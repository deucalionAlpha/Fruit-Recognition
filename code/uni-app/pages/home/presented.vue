<template>
	<view class="content">
		<view class="presented-item" v-for="(item,index) in presented" :key= index>
			<view class="presented-icon">
				<view class="iconfont" :class="item.iconName"></view>
			</view>
			<view class="presented-text">
				<view class="presented-title">{{item.title}}</view>
				<view class="presented-introduce">{{item.introduce}}</view>
			</view>
			<button class="button presented-btn">{{item.btnName}}</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				presented: [
					{
						iconName: "icon-hongbao1",
						title: "咖啡红包",
						introduce: "可单发可群发 全新社交利器",
						btnName: "发红包"
					},
					{
						iconName: "icon-liwu1",
						title: "咖啡请客",
						introduce: "一对一送Ta咖啡 为友谊干杯",
						btnName: "请Ta喝"
					},
					{
						iconName: "icon-yaoqing",
						title: "邀请得杯",
						introduce: "邀请新朋友 你和Ta各得一杯",
						btnName: "马上分享"
					}
				]
			};
		}
	}
</script>

<style>
	.content{padding: 0 24upx;border-top: 1px solid #e7e7e7;}
	.presented-item{background-color: #fff;padding: 32upx 38upx;margin-top: 40upx;display: flex;border-radius: 8upx;justify-content: space-between;}
	.presented-icon{width: 68upx;height: 68upx;border: 4upx solid #f1e6e1;border-radius: 50%;text-align: center;margin-right: 20upx;}
	.presented-icon .iconfont{color: #a08066;font-size: 36upx;line-height: 68upx;}
	.presented-text{flex-grow: 2;}
	.presented-title{font-size: 32upx;line-height: 44upx;}
	.presented-introduce{color: #999;font-size: 24upx;line-height: 24upx;}
	.presented-btn{width: 140upx;height: 54upx;font-size: 22upx;line-height: 54upx;margin-top: 11upx;padding: 0;}
</style>
