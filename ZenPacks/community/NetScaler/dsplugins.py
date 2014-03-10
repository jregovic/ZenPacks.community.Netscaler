from pprint import pprint
from Products.ZenEvents import ZenEventClasses
from ZenPacks.zenoss.PythonCollector.datasources.PythonDataSource \
	import PythonDataSourcePlugin
from twisted.internet import defer

class NetScalerPlugin(PythonDataSourcePlugin):
	"""Explanation of what MyPlugin does."""
	lbvserver_vars=['actsvcs',
		'curclntconnections',
		'cursrvrconnections',
		'deferredreq',
		'deferredreqrate',
		'establishedconn',
		'hitsrate',
		'inactsvcs',
		'invalidrequestresponse',
		'invalidrequestresponsedropped',
		'pktsrecvdrate',
		'pktssentrate',
		'requestbytesrate',
		'requestsrate',
		'responsebytesrate',
		'responsesrate',
		'totalpktsrecvd',
		'totalpktssent',
		'totalrequestbytes',
		'totalrequests',
		'totalresponsebytes',
		'totalresponses',
		'tothits',
		'totspillovers',
		'vslbhealth']
		
	# List of device attributes you'll need to do collection.
	proxy_attributes = (
		'zNetScalerUser',
		'zNetScalerPassword',
		)
 
	@classmethod
	def config_key(cls, datasource, context):
		"""
		Return a tuple defining collection uniqueness.
 
		This is a classmethod that is executed in zenhub. The datasource and
		context parameters are the full objects.
 
		This example implementation is the default. Split configurations by
		device, cycle time, template id, datasource id and the Python data
		source's plugin class name.
 
		You can omit this method from your implementation entirely if this
		default uniqueness behavior fits your needs. In many cases it will.
		"""
		pprint(datasource)
		pprint(context)
		return (
			context.device().id,
			datasource.getCycleTime(context),
			datasource.rrdTemplate().id,
			datasource.id,
			datasource.plugin_classname,
			)
 
	@classmethod
	def params(cls, datasource, context):
		"""
		Return params dictionary needed for this plugin.
 
		This is a classmethod that is executed in zenhub. The datasource and
		context parameters are the full objects.
 
		This example implementation will provide no extra information for
		each data source to the collect method.
 
		You can omit this method from your implementation if you don't require
		any additional information on each of the datasources of the config
		parameter to the collect method below. If you only need extra
		information at the device level it is easier to just use
		proxy_attributes as mentioned above.
		"""
		return {}


		
	def collect(self, config):
		"""
		No default collect behavior. You must implement this method.
 
		This method must return a Twisted deferred. The deferred results will
		be sent to the onResult then either onSuccess or onError callbacks
		below.
		"""
		
		pprint(config)		
		ds0 = config.datasources[0]
	
		pprint(ds0)	
		return defer.returnValue([1])
 
	def onResult(self, result, config):
		"""
		Called first for success and error.
 
		You can omit this method if you want the result of the collect method
		to be used without further processing.
		"""
		return result
 
	def onSuccess(self, result, config):
		"""
		Called only on success. After onResult, before onComplete.
 
		You should return a data structure with zero or more events, values
		and maps.
		"""
		return {
			'events': [{
				'summary': 'successful collection',
				'eventKey': 'myPlugin_result',
				'severity': ZenEventClasses.Clear,
				},{
				'summary': 'first event summary',
				'eventKey': 'myPlugin_result',
				'severity': ZenEventClasses.Info,
				},{
				'summary': 'second event summary',
				'eventKey': 'myPlugin_result',
				'severity': ZenEventClasses.Warning,
				}],
 
			'values': {
				None: {  # datapoints for the device (no component)
					'datapoint1': 123.4,
					'datapoint2': 5.678,
					},
				'cpu1': {
					'user': 12.1,
					'system': 1.21,
					'io': 23,
					}
				},
 
			'maps': [
				ObjectMap(...),
				RelationshipMap(..),
				]
			}
 
	def onError(self, result, config):
		"""
		Called only on error. After onResult, before onComplete.
 
		You can omit this method if you want the error result of the collect
		method to be used without further processing. It recommended to
		implement this method to capture errors.
		"""
		return {
			'events': [{
				'summary': 'error: %s' % result,
				'eventKey': 'myPlugin_result',
				'severity': 4,
				}],
			}
 
	def onComplete(self, result, config):
		"""
		Called last for success and error.
 
		You can omit this method if you want the result of either the
		onSuccess or onError method to be used without further processing.
		"""
		return result
 
	def cleanup(self, config):
		"""
		Called when collector exits, or task is deleted or changed.
		"""
		return

