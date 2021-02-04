import pyodbc

def get_communicating_meter_cbconnected_localdisconnect_enabled():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=HAHESSQL02DEV;'
                          'Database=AMST_05_meteringware;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('''
    select Top 1 DeviceCode, MeteringPointCode from (
    select top 10 * from (
    SELECT TOP (1000) d.[Id]
    ,d.Code [DeviceCode]
          ,dc.Id [dcId]
          ,dc.DeviceId dcDEviceId
          ,dc.Code [dcCode]
          ,CBLocalReconnect.[Value] [CB Local Reconnect]
          ,CBLocalDisconnect.[Value] [CB Local Disconnect]
          ,CBConnection.[Value] [CB Connection]
          ,mpd.DeviceCode MPD
          ,mp.MeteringPointCode
          ,mp.StreetAddress
          ,dct.LastCommunication

      FROM [AMST_05_Meteringware].[dbo].[Devices] d

      inner join AMST_05_Gateware.dbo.MeteringPointDevices mpd on (mpd.DeviceCode = d.Code and mpd.IsDeleted =0)
      left join AMST_05_Meteringware.dbo.DeviceComponents dc on (dc.DeviceId = d.Id and dc.Discriminator = 'MeterEntity')
      left join AMST_05_Gateware.dbo.MeteringPoints mp on mp.MeteringPointId = mpd.MeteringPointId

      left join AMST_05_Meteringware.dbo.DeviceComponentProperties CBLocalReconnect 
        on (CBLocalReconnect.ComponentId = dc.Id
            AND CBLocalReconnect.[Key] = 'CircuitBreakerLocalReconnect')

    left join AMST_05_Meteringware.dbo.DeviceComponentProperties CBLocalDisconnect 
        on (CBLocalDisconnect.ComponentId = dc.Id
            AND CBLocalDisconnect.[Key] = 'CircuitBreakerLocalDisconnect')

    left join AMST_05_Meteringware.dbo.DeviceComponentProperties CBConnection 
        on (CBConnection.ComponentId = dc.Id
            AND CBConnection.[Key] = 'CircuitBreakerConnection')
    left join AMST_05_Meteringware.dbo.DeviceCommunicationTopologies dct on dct.DeviceId = d.Id
    )xx
    where [CB Local Disconnect] = 'Enabled'
    AND [CB Connection] = 'Connected'
    AND LastCommunication > getdate() - 0.1
    ) xy
    order by LastCommunication asc
    ''')

    retval = ''
    for row in cursor:
        retval = row
        # print(row)
        break

    print('About to return ')
    print(retval)
    conn.close()
    return retval


if __name__ == "__main__":
    print("retval = ")
    print(get_communicating_meter_cbconnected_localdisconnect_enabled())

