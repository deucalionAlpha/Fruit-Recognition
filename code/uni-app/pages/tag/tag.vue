<template>
	<view>
		<view class="uni-flex uni-column">
			<view class="button-view flex-item flex-item-V"  >
				<button type="default" class="chooseImage" hover-class="hover" formType="submit" @click="ImgProcess">上传图片</button>
			</view>
			<view class="text uni-flex" style="-webkit-flex: 1;flex: 1;height: 200rpx;-webkit-justify-content: center;justify-content: center;-webkit-align-items: center;align-items: center;">
				{{this.message}}
			</view>
			
			<view>
				<image style="width: 400px; height: 300px; background-color: #eeeeee;" :mode="aspectFit" :src=this.src @error="imageError"></image>
			</view>
			
			<view v-if="flag!=1"class="text uni-flex" style="-webkit-flex: 1;flex: 1;height: 200rpx;-webkit-justify-content: center;justify-content: center;-webkit-align-items: center;align-items: center;">
				图片中水果为{{this.type}} 糖度检测结果为{{this.percentage}}
			</view>
			
			<view v-if="flag!=1" class="button-view flex-item flex-item-V" >
				<button type="default" hover-class="hover" formType="submit" @click="Insugar">加入每日糖分摄入量</button>
			</view>
		</view>

	
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				message:'您还未上传图片',
				desc:'',
				flag:1,
				type:'',
				percentage:'',
				src:''
			}
		},
		methods: {	
			Insugar()
			{
				uni.showModal({
				    title: '提示',
				    content: '已加入每日糖分摄入量',
				    success: function (res) {
				        if (res.confirm) {
				            console.log('用户点击确定');
				        } else if (res.cancel) {
				            console.log('用户点击取消');
				        }
				    }
				});
			},
			ImgProcess()
			{
				this.chooseImage();
			},
			chooseImage() {
				let _self = this;
				console.log("in the choose function");
				uni.chooseImage({
					count: 1, //默认9
					sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
					sourceType: ['album','camera'], //从相册选择、摄像头  选择摄像头的时候还不行
					success: function(res) {
						console.log(JSON.stringify(res.tempFilePaths));
						console.log("图片选择成功");
						_self.message="图片选择成功";
						_self.src = res.tempFilePaths[0];
						_self.type = "识别中.."
						_self.percentage = "识别中.."
						_self.flag = 0;
						console.log("上传图片地址为");
						console.log(_self.src);
						let _self_2 = _self;
						uni.uploadFile({
							url:"http://120.79.35.153/api/customers/recognize",
							filePath: _self.src,
							name: 'file',
							formData: {
								'user': 'test'
							},
							success: (uploadFileRes) => {
								let result = JSON.parse(uploadFileRes.data);
								console.log(result);//甜度数据
								_self_2.type=result.type;
								_self_2.percentage=result.percentage.toFixed(3);
								
							}
						});
					}
				});

			},
			imageError: function(e) {
				console.error('image发生error事件，携带值为' + e.detail.errMsg)
			}
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
