#!/usr/bin/env python

diodes = []

for i in xrange(6, 12):
	colomn = ['D'+str(j+1)+' ' for j in range(10*i, 10*(i+1))]
	diodes.append(colomn)

# print diodes

with open('LED_matrix.kicad_pcb', 'r') as f:
	raw_lines = f.read().split('\n')

# print raw_lines

txt_begin = 'fp_text reference '
origin = [125.1, 88.25]

for n in xrange(len(diodes)):
	colomn = diodes[n]
	for k in xrange(len(colomn)):
		diode = colomn[k]
		for i in xrange(len(raw_lines)):
			if txt_begin+diode in raw_lines[i]:
				old_pos = raw_lines[i-5].split('at')[1][:-1]
				new_x = origin[0] + 1.2*n
				new_y = origin[1] + 1.2*k
				# print str(new_x)+' '+str(new_y)+' 135', diode, old_pos
				raw_lines[i-5] = raw_lines[i-5].replace(old_pos, ' '+str(new_x)+' '+str(new_y)+' 135')
				print diode, raw_lines[i-5]
				for j in xrange(24):
					if '180' in raw_lines[i+j]:
						raw_lines[i+j] = raw_lines[i+j].replace('180', '135')
						print raw_lines[i+j], 'll'

out = '\n'.join(raw_lines)

with open('LED_matrix.kicad_pcb', 'w') as f:
    f.write(out)