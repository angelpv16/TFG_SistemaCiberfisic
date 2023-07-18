from kepconfig import connection
from kepconfig.connectivity import tag


server = connection.server(host = '127.0.0.1', port = 57412, user = 'Administrator', pw = '')


# from kepconfig.connectivity import channel

# channel_data = {"common.ALLTYPES_NAME": "Channelz","servermain.MULTIPLE_TYPES_DEVICE_DRIVER": "Simulator"}
# result = channel.add_channel(server,channel_data)


tag_info = [
    {
            "common.ALLTYPES_NAME": "Temp",
            "servermain.TAG_ADDRESS": "R0"
    },
    {
            "common.ALLTYPES_NAME": "Temp2",
            "servermain.TAG_ADDRESS": "R1"
    }
]
tag_path = '{}.{}.{}'.format("FX3U", "FX","Variables")
result = tag.add_tag(server, tag_path, tag_info)
