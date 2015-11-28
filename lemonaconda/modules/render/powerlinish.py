# -*- coding: utf-8 -*-

POWERLINE_ARROW_FORMAT = '%{{F#{bgcolor}}}%{{R}}{0}%{{R}}%{{F#{fgcolor}}}'

class PowerlineRenderer:
    def render(self, panel):
        string = '%{{F#{0}}}'.format(panel._fgcolor)
        for index, seg in enumerate(panel._segments):
            if 'alignment' in seg.properties:
                if seg.properties['alignment'] is 'left':
                    align='l'
                elif seg.properties['alignment'] is 'right':
                    align='r'
                elif seg.properties['alignment'] is 'center':
                    align='c'
                else:
                    pass
                    # Raise error
                string += "%{{{0}}}".format(align)
            string += '%{{B#{0}}}'.format(seg.properties['bgcolor'])
            if seg.properties['pl_left']:
                if index > 0:
                    color = panel._segments[index-1].properties['bgcolor']
                else:
                    color = panel._bgcolor
                string += POWERLINE_ARROW_FORMAT.format('',
                                                        fgcolor=panel._fgcolor,
                                                        bgcolor=color,
                                                        )
            string += seg.get_output()
            if seg.properties['pl_right']:
                if index < len(panel._segments) - 1:
                    color = panel._segments[index+1].properties['bgcolor']
                else:
                    color = panel._bgcolor
                string += POWERLINE_ARROW_FORMAT.format('',
                                                        fgcolor=panel._fgcolor,
                                                        bgcolor=color,
                                                        )
            string += '%{B-}'
        return string
