import logging
LOG = logging.getLogger('zen.NetScaler')

from twisted.internet.defer import DeferredList

from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap

from pprint import pprint
import nsnitro
from nsnitro.nsnitro import *
from nsnitro.nsresources.nsconfig import NSConfig
from nsnitro.nsutil import *

class NetScaler(PythonPlugin):
	deviceProperties = PythonPlugin.deviceProperties + (
		'zNetScalerUser',
		'zNetScalerPassword'
		)

	def collect(self,device,unused):
		if not device.zNetScalerUser:
			LOG.error('zNetScalerUser is not set. Not discovering')
			return None

		if not device.zNetScalerPassword:
			LOG.error('zNetScalerPassword is not set. Not discovering.')
			return None
		client=NSNitro(device.manageIp,device.zNetScalerUser,device.zNetScalerPassword,useSSL=True)
		
		if not client.login():
			LOG.error('Could not login')
			return None
		url = 'https://%s/nitro/v1/stat/lbvserver' % (device.manageIp)
		info=client.get(url)
	
		return info
	
	def process(self, device, results, unused):
		lbvservers = len(results.get_json_response()['lbvserver'])
		
		rm = self.relMap()
		lbvmaps=[]	
		for lbv in results.get_json_response()['lbvserver']:
			name = lbv['name']
			primaryipaddress = lbv['primaryipaddress']
			state = lbv['state']
			vipType = lbv['type']

			if not name:
				log.warn('skipping VIP with no name')
				continue
			lbvmaps.append(ObjectMap(data=dict(	
				id=self.prepId(name),
				title=name,
				name=name,
				primaryipaddress=primaryipaddress,
				state=state,
				vipType=vipType,
			)))

		#relMap=self.relMap()
		#relMap.append(lbvmaps)
		relMap= RelationshipMap(
			relname='lbvservers',
			modname='ZenPacks.community.NetScaler.LbVServer',
			objmaps=lbvmaps)
		#pprint(relMap)
		return relMap
