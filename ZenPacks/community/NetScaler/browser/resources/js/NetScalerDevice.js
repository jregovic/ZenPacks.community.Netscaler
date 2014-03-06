(function(){
 
var ZC = Ext.ns('Zenoss.component');
 
ZC.registerName(
    'NetScalerLbvServer',
    _t('LB VServer'),
    _t('LB VServers'));

ZC.NetScalerLbvServerPanel = Ext.extend(ZC.ComponentGridPanel, {
 constructor: function(config) {
 config = Ext.applyIf(config||{}, {
 componentType: 'NetScalerLbvServer',
 autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'primaryipaddress'},
                {name: 'vipType'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'primaryipaddress',
                dataIndex: 'primaryipaddress',
                header: _t('Primary IP'),
                sortable: true,
                width: 120
            },{
                id: 'vipType',
                dataIndex: 'vipType',
                header: _t('VIP Type'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });
 
        ZC.NetScalerLbvServerPanel.superclass.constructor.call(
 this, config);
    }
});
 
Ext.reg('NetScalerLbvServerPanel', ZC.NetScalerLbvServerPanel); 
})();
