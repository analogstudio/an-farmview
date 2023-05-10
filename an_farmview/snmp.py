import pysnmp.hlapi

from .config import settings

def get_sensor(oid):
    """Simon not knowing how to use iterators properly
    but using this example code works so bundling it into a func!
    """

    iterator = pysnmp.hlapi.getCmd(
        pysnmp.hlapi.SnmpEngine(),
        pysnmp.hlapi.CommunityData(settings.snmp_community),
        pysnmp.hlapi.UdpTransportTarget((settings.snmp_ip, 161)),
        pysnmp.hlapi.ContextData(),
        pysnmp.hlapi.ObjectType(pysnmp.hlapi.ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        
    if errorIndication:  # SNMP engine errors
        print(errorIndication)
    else:
        if errorStatus:  # SNMP agent errors
            print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
        else:
            for varBind in varBinds:  # SNMP response contents
                # print(' = '.join([x.prettyPrint() for x in varBind]))
                value = int(str(varBind).split(' ')[-1])
                return value

def get_temperature_rear():
    oid_1_name = '1.3.6.1.4.1.318.1.1.10.4.2.3.1.3.0.1'
    oid_1_location = '1.3.6.1.4.1.318.1.1.10.4.2.3.1.4.0.1'
    oid_1_temp = '1.3.6.1.4.1.318.1.1.10.4.2.3.1.5.0.1'

    temperature_rear = get_sensor(oid_1_temp)

    return temperature_rear

def get_temperature_front():

    oid_2_name = '1.3.6.1.4.1.318.1.1.10.4.2.3.1.3.0.2'
    oid_2_location = '1.3.6.1.4.1.318.1.1.10.4.2.3.1.4.0.2'
    oid_2_temp = '1.3.6.1.4.1.318.1.1.10.4.2.3.1.5.0.2'

    temperature_front = get_sensor(oid_2_temp)

    return temperature_front

if __name__ == '__main__':
    print('{n} - temperature_rear: {v}'.format(n=__name__, v=get_temperature_rear()))
    print('{n} - temperature_front: {v}'.format(n=__name__, v=get_temperature_front()))
    