from numpy import int8


def objid_extract(obj_id):
    
    masks = {'sky_version': 0x7800000000000000,
            'rerun':0x07FF000000000000,
            'run': 0x0000FFFF00000000,
            'camcol': 0x00000000E0000000,
            'first_field':0x0000000010000000,
            'field': 0x000000000FFF0000,
            'object_id': 0x000000000000FFFF}
    
    sky_version = (obj_id & masks['sky_version']) >> 59
    rerun = (obj_id & masks['rerun']) >> 48
    run = (obj_id & masks['run']) >> 32
    camcol = (obj_id & masks['camcol']) >> 29
    first_field = (obj_id & masks['first_field']) >> 28
    field = (obj_id & masks['field']) >> 16
    object_id = (obj_id & masks['object_id']) >> 0
    
    
    return {'sky_version': sky_version,
            'rerun': rerun,
            'run': run,
            'camcol':camcol,
            'first_field': first_field,
           'field': field,
           'object_id': object_id
           }
    
def objid_merge(sky = 15, run, rerun, camcol, field, object_id):
    superid: int8 = 0
    superid = (superid | (sky << 59) | (rerun << 48) | (run << 32) | (camcol << 29) | (0 << 28) | (field << 16) | (object_id << 0))
    return superid