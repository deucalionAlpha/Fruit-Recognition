<template>
	<view class="center uni-padding-wrap uni-common" style="padding-left: 0upx;">
		<view class="logo" style="display: flex;" @click="goLogin" :hover-class="!login ? 'logo-hover' : ''">
			<image class="logo-img" :src="login ? uerInfo.avatarUrl :avatarUrl"></image>
			<view class="logo-title">
				<text class="uer-name">Hi，{{login ? uerInfo.name : '您未登录'}}</text>
				<text class="go-login navigat-arrow" v-if="!login">&#xe65e;</text>
			</view>
		</view>


		<view class="center-list">
			<view class="uni-flex uni-row">
				<view class="text" style="-webkit-flex: 1;flex: 1.2;">
					<text>今日糖分摄入:12</text>
				</view>
				<view class="text" style="-webkit-flex: 1;flex: 1.2;">今日活跃度:323</view>
				<view class="text" style="-webkit-flex: 1;flex: 1;">积分: 668</view>
			</view>
			<view class="center-list-item border-bottom" @click="Sign">
				<text class="list-icon">&#xe60c;</text>
				<text class="list-text">今日打卡</text>
				<text class="navigat-arrow">&#xe65e;</text>
			</view>
			<view class="center-list-item">
				<text class="list-icon">&#xe60d;</text>
				<text class="list-text">今日健康标准</text>
				<text class="navigat-arrow">&#xe65e;</text>
			</view>
			<view class="center-list-item">
				<text class="list-text">糖分摄入：64</text>
			</view>
		</view>

		
		<view class="center-list">
			<view class="center-list-item">
				<text class="list-icon">&#xe609;</text>
				<text class="list-text">账号管理</text>
				<text class="navigat-arrow">&#xe65e;</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				login: false,
				avatarUrl: '/static/logo.png',
				uerInfo: {}
			}
		},
		methods: {
			goLogin() {
				if (!this.login) {
					uni.navigateTo({
						url: '/pages/login/login'
					});
				}
			},
			Sign() {
				if (!this.login) {
					uni.navigateTo({
						url: '/pages/login/signin'
					});
				}
			},
		}
	}
</script>

<style>
	.flex-item {
		width: 33.3%;
		height: 200rpx;
		text-align: center;
		line-height: 200rpx;
	}

	.flex-item-V {
		width: 100%;
		height: 150rpx;
		text-align: center;
		line-height: 150rpx;
	}

	.text {
		margin: 15rpx 10rpx;
		padding: 0 20rpx;
		background-color: #ebebeb;
		height: 70rpx;
		line-height: 70rpx;
		text-align: center;
		color: #777;
		font-size: 26rpx;
	}

	.desc {
		/* text-indent: 40rpx; */
	}
</style>
