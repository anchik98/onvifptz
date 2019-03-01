#Этот файл содержит код для получения информации о PTZ камере и 
# ее абсолютное перемещение через командную строку Python 2.7

from onvif import ONVIFCamera

#Подключение к камере и знакомство с возможностями/ограничениями PTZ
#Connecting
#mycam = ONVIFCamera('192.168.15.42', 80, 'admin', 'passw', 'C:/Python27/onvif/wsdl')
mycam = ONVIFCamera('192.168.15.42', 80, 'anchik981', 'qDOyrQN278IxC0nT', 'C:/Python27/onvif/wsdl')
print mycam.devicemgmt.GetDeviceInformation()

# Creating media service
media_service = mycam.create_media_service()
# Getting profiles
profiles = media_service.GetProfiles()
media_profile = profiles[0]
print 'Profiles: ', media_profile
# Getting token
token = media_profile._token
print 'Token: ', token 

# Create ptz service object
ptz = mycam.create_ptz_service()
#Get available PTZ services
request = ptz.create_type('GetServiceCapabilities')
Service_Capabilities = ptz.GetServiceCapabilities(request)
print 'PTZ service capabilities:', Service_Capabilities
#Get PTZ status
status = ptz.GetStatus({'ProfileToken':token})
#Current coordinates
print 'PTZ status:', status
print 'Pan position:', status.Position.PanTilt._x
print 'Tilt position:', status.Position.PanTilt._y
print 'Zoom position:', status.Position.Zoom._x


# Get PTZ configuration options for getting option ranges
request = ptz.create_type('GetConfigurationOptions')
request.ConfigurationToken = media_profile.PTZConfiguration._token
ptz_configuration_options = ptz.GetConfigurationOptions(request)
print 'PTZ configuration options:', ptz_configuration_options

#Absolute move: диагностика и перемещение

request_absolute_move = ptz.create_type('AbsoluteMove')
request_absolute_move.ProfileToken = media_profile._token
print 'Absolute move options: ', request_absolute_move

#Absolute pan-tilt (pan position, tilt position, velocity)
# position 1
pan = -0.4
tilt = -1
velocity = 0.6

# position 2
pan = 0.4
tilt = -0.8
velocity = 0.3

request_absolute_move.Position.PanTilt._x = pan
request_absolute_move.Position.PanTilt._y = tilt
request_absolute_move.Speed.PanTilt._x = velocity
request_absolute_move.Speed.PanTilt._y = velocity

print 'Absolute move to:', request_absolute_move.Position
print 'Absolute speed:',request_absolute_move.Speed
# Moving
ptz.AbsoluteMove(request_absolute_move)
print 'Absolute move pan-tilt requested:', pan, tilt, velocity
#Get current position
status = ptz.GetStatus({'ProfileToken':token})
#Show Current coordinates
print 'PTZ status:', status
