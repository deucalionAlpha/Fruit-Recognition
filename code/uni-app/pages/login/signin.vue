<template>
	<view >
		<image style="align-items: center; justify-content: center; width: 400px; height: 300px; background-color: #eeeeee;" :mode="aspectFit" :src="avatarUrl"  @error="imageError"></image>
		<view class="text uni-flex" style="-webkit-flex: 1;flex: 1;height: 200rpx;-webkit-justify-content: center;justify-content: center;-webkit-align-items: center;align-items: center;">
			今日已打卡！
		</view>
	</view>
</template>





<script>
	export default {
		data() {
			return {
				avatarUrl: '/static/yes.png',
			}
		},
		methods: {
			login(e) {
				console.log("得到账号:"+ e.detail.value.nameValue + ';得到密码:' + e.detail.value.passwordValue)
			},
			register() {
				console.log("前往注册页面")
			}
		}
	}
</script>

