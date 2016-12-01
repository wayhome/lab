#!/usr/bin/env python
# encoding: utf-8
import struct
import binascii

values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values
print 'Format string  :', s.format
print 'Uses           :', s.size, 'bytes'
print 'Binary data    :', packed_data
print 'Packed Value   :', binascii.hexlify(packed_data)
