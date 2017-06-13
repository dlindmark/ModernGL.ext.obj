'''
    ModernGL extension for loading obj files
'''

import logging
import re
import struct

log = logging.getLogger('ModernGL.ext.obj')


def loads(text, texcoords=True, normals=True, *, xyz=tuple) -> bytes:
    '''
        Load obj from string.

        Args:
            text (str): The obj file's content.
            texcoords (bool): Include texture coordinates in the result.
            normals (bool): Include normals in the result.

        Keyword Args:
            xyz (lambda): Called on v, vn and vt.
    '''

    lines = [x.strip() for x in text.splitlines()]
    lines = filter(lambda x: x and not x.startswith('#'), lines)

    obj = {
        'v': [None],
        'vn': [None],
        'vt': [None],
    }

    data = bytearray()

    for line in lines:
        match = re.match(r'^(v[nt]?)\s+(-?\d+(\.\d+)?)\s+(-?\d+(\.\d+)?)\s+(-?\d+(\.\d+)?)$', line)
        if match:
            obj[match.group(1)].append(xyz(map(float, match.group(2, 4, 6))))
            continue

        match = re.match(r'^f\s+(\d+)(/(\d+)?(/(\d+))?)?\s+(\d+)(/(\d+)?(/(\d+))?)?\s+(\d+)(/(\d+)?(/(\d+))?)?$', line)
        if match:
            for v, vt, vn in (match.group(1, 3, 5), match.group(6, 8, 10), match.group(11, 13, 15)):
                data.extend(struct.pack('3f', *obj['v'][int(v)]))
                if vt is not None and texcoords:
                    data.extend(struct.pack('3f', *obj['vt'][int(vt)]))
                if vn is not None and normals:
                    data.extend(struct.pack('3f', *obj['vt'][int(vt)]))
            continue

        log.debug('unknown line: "%s"', line)

    return bytes(data)


def load(filename, *, texcoords=True, normals=True, xyz=tuple) -> bytes:
    '''
        Load obj from string.

        Args:
            text (str): The obj file's content.
            texcoords (bool): Include texture coordinates in the result.
            normals (bool): Include normals in the result.

        Keyword Args:
            xyz (lambda): Called on v, vn and vt.
    '''

    with open(filename, 'r') as f:
        return loads(f.read(), texcoords, normals, xyz=xyz)
