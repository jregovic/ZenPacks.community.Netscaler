from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
 
 
class LbVServer(DeviceComponent,ManagedEntity):
	meta_type= portal_type = 'NetScalerLbvServer'

	name = None
	primaryipaddress = None
	state = None
	vipType = None

	_properties = ManagedEntity._properties + (
		{'id': 'name','type':'string'},
		{'id': 'primaryipaddress','type':'string'},
		{'id': 'state','type':'string'},
		{'id': 'vipType','type':'string'},
		)

	_relations = ManagedEntity._relations + (
		('lbvserver_device',ToOne(ToManyCont,
			'ZenPacks.community.NetScaler.NetScalerDevice',
			'lbvservers',
			)),
		)

	factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

	def device(self):
		return self.lbvserver_device()

	def getRRDTemplateName(self):
		return 'lbvserver'
