# TODO: Enable when sound.nx is included #

# import os

# from nxpy.nxfile import NXFile


# def test_nxsound():
#     node = NXFile(os.path.join(os.path.dirname(__file__),  'sound002.nx')).resolve(
#         "Bgm34.img/MapleLeaf")
#     sound = node.get_sound()
#     byte = sound.get_data()
#     assert node.name == 'MapleLeaf'
#     print(node.length)
#     print(len(byte))
#     assert node.length == 1291315
#     assert len(byte) == 22777422
