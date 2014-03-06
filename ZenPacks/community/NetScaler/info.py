# This file is the conventional place for "Info" adapters. Info adapters are
# a crucial part of the Zenoss API and therefore the web interface for any
# custom classes delivered by your ZenPack. Examples of custom classes that
# will almost certainly need info adapters include datasources, custom device
# classes and custom device component classes.

# Mappings of interfaces (interfaces.py) to concrete classes and the factory
# (these info adapter classes) used to create info objects for them are managed
# in the configure.zcml file.

from zope.component import adapts
from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos.template import RRDDataSourceInfo

#from ZenPacks.NAMESPACE.PACKNAME.ExampleComponent import ExampleComponent
from ZenPacks.community.NetScaler.interfaces \
    import INetScalerDeviceInfo, ILbVServerInfo

class NetScalerDeviceInfo(DeviceInfo):
	implements(INetScalerDeviceInfo)

	lbvserver_count = ProxyProperty('lbvserver_count')

class LbVServerInfo(ComponentInfo):
	implements(ILbVServerInfo)
	
	name = ProxyProperty('name')
        primaryipaddress = ProxyProperty('primaryipaddress')
        state = ProxyProperty('state')
        vipType = ProxyProperty('vipType')

	def status(self):
		if self.state == 'DOWN':
			return 'Down'
		else:
			return 'Up'

