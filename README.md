![Version](https://img.shields.io/github/v/release/chliny/hass-volvooncall-cn-aaos?color=green&label=Version)
[![GitHub all releases](https://img.shields.io/github/downloads/chliny/hass-volvooncall-cn-aaos/total?label=Downloads)](https://github.com/chliny/hass-volvooncall-cn-aaos/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)


# Volvo On Call CN AAOS
Homeassistant volvooncall 中国区安卓车机版插件

# 实体一览
`{vin}` 表示车架号
| ID                                          | 名称               | 备注                                                                                                                                     |
|---------------------------------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `lock.{vin}_lock`                           | 车锁               | 远程锁定或解锁车辆 |
| `lock.{vin}_window_lock`                    | 车窗               | 远程开窗或关窗|
| `sensor.{vin}_engine`                       | 引擎               |                                                                                                                                          |
| `sensor.{vin}_distance_to_empty`            | 续航里程           |                                                                                                                                          |
| `binary_sensor.{vin}_lock`                  | 车锁状态           |                                                                                                                                          |
| `binary_sensor.{vin}_front_left_door`       | 前左门             | 表示门是否打开                                                                                                                           |
| `binary_sensor.{vin}_front_right_door`      | 前右门             |                                                                                                                                          |
| `binary_sensor.{vin}_rear_left_door`        | 后左门             |                                                                                                                                          |
| `binary_sensor.{vin}_rear_right_door`       | 后右门             |                                                                                                                                          |
| `binary_sensor.{vin}_front_left_window_open`| 前左窗             | 表示窗是否打开                                                                                                                           |
| `binary_sensor.{vin}_front_right_window_open` | 前右窗             |                                                                                                                                          |
| `binary_sensor.{vin}_rear_left_window`      | 后左窗             |                                                                                                                                          |
| `binary_sensor.{vin}_rear_right_window`     | 后右窗             |                                                                                                                                          |
| `sensor.{vin}_fuel_amount`                  | 油箱剩余油量       |                                                                                                                                          |
| `binary_sensor.{vin}_hood`                  | 引擎盖             | 表示引擎盖是否打开                                                                                                                       |
| `sensor.{vin}_odometer`                     | 总里程             |                                                                                                                                          |
| `binary_sensor.{vin}_sunroof`               | 天窗               |                                                                                                                                          |
| `binary_sensor.{vin}_tail_gate`             | 尾门               |                                                                                                                                          |
| `device_tracker.{vin}_position`             | 位置               |                                                                                                                                          |
| `device_tracker.{vin}_position_wgs84`       | 位置 wgs84 坐标    | 在 ha 默认地图上展示车辆时，请使用此实体                                                                                                 |

# 测试车型
- 2024 XC60

# HACS 安装集成
HACS -> 集成 -> 右上角三个点 -> 自定义存储库
- 存储库：https://github.com/chliny/hass-volvooncall-cn-aaos
- 类别：集成

浏览并下载存储库 -> 搜索 Volvo On Call CN AAOS 并下载

# Homeassistant 添加集成
设置 -> 设备与服务 -> 添加集成 -> 搜索品牌 Volvo On Call CN AAOS -> 填入手机号和密码
- 手机号：11 位纯数字
- 密码：即“沃尔沃APP”上的登录密码，需要提前设置好登录密码

提交稍等片刻后，即可看到拥有的车辆设备

# 效果预览
<img src="images/screenshot-20230729-011246.png" alt="" width="50%"/>
<img src="images/screenshot-20230729-011320.png" alt="" width="50%"/>
