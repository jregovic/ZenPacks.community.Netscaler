from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class NetScalerDevice(Device):
	lbvserver_count = None

	_properties = Device._properties + (
		{'id':'lbvserver_count','type':'int'},
		)

        _relations = Device._relations + (
                ('lbvservers',ToManyCont(ToOne,
                        'ZenPacks.community.NetScaler.LbVServer',
                        'lbvserver_device',
                        )),
                )

