import os

from nxpy.nxfile import NXFile


def test_nxfile():
    # ['base.nx', 'character.nx', 'effect.nx', 'etc.nx', 'item.nx',
    #  'map.nx', 'mob.nx', 'morph.nx', 'npc.nx', 'quest.nx',
    #  'reactor.nx', 'skill.nx', 'sound.nx', 'string.nx', 'tamingmob.nx',
    #  'ui.nx']
    nx_files = ['map.nx']
    for nx_file in nx_files:
        file = NXFile(os.path.join(os.path.dirname(__file__), nx_file))
        assert isinstance(file, NXFile)
