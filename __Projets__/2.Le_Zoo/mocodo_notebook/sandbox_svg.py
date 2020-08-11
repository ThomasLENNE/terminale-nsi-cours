#!/usr/bin/env python
# encoding: utf-8
# Généré par Mocodo 2.3.8 le Mon, 10 Aug 2020 22:57:53

from __future__ import division
from math import hypot

import time, codecs

(width,height) = (690,553)
cx = {
    u"VERSER"     :   77,
    u"MEMBRE"     :  225,
    u"RECENSER"   :  364,
    u"ESPECE"     :  496,
    u"VIVRE_LIBRE":  627,
    u"DATEHEURE"  :   77,
    u"VISITER"    :  225,
    u"VETERINAIRE":  364,
    u"DF1"        :  496,
    u"PAYS"       :  627,
    u"CONTROLER"  :   77,
    u"HEBERGER"   :  225,
    u"SPECIALISER":  364,
    u"PROVENIR"   :  496,
    u"DF2"        :  627,
    u"CONTROLEUR" :   77,
    u"PARC"       :  225,
    u"ANIMAL"     :  364,
    u"DESCENDRE"  :  496,
    u"CONTINENT"  :  627,
}
cy = {
    u"VERSER"     :   62,
    u"MEMBRE"     :   62,
    u"RECENSER"   :   62,
    u"ESPECE"     :   62,
    u"VIVRE_LIBRE":   62,
    u"DATEHEURE"  :  211,
    u"VISITER"    :  211,
    u"VETERINAIRE":  211,
    u"DF1"        :  211,
    u"PAYS"       :  211,
    u"CONTROLER"  :  333,
    u"HEBERGER"   :  333,
    u"SPECIALISER":  333,
    u"PROVENIR"   :  333,
    u"DF2"        :  333,
    u"CONTROLEUR" :  464,
    u"PARC"       :  464,
    u"ANIMAL"     :  464,
    u"DESCENDRE"  :  464,
    u"CONTINENT"  :  464,
}
shift = {
    u"VERSER,MEMBRE"          :    0,
    u"VERSER,DATEHEURE"       :    0,
    u"RECENSER,ESPECE"        :    0,
    u"RECENSER,DATEHEURE"     :    0,
    u"VIVRE_LIBRE,PAYS"       :    0,
    u"VIVRE_LIBRE,ESPECE"     :    0,
    u"VISITER,VETERINAIRE"    :    0,
    u"VISITER,ANIMAL"         :    0,
    u"VISITER,DATEHEURE"      :    0,
    u"DF1,ANIMAL"             :    0,
    u"DF1,ESPECE"             :    0,
    u"CONTROLER,CONTROLEUR"   :    0,
    u"CONTROLER,PARC"         :    0,
    u"CONTROLER,DATEHEURE"    :    0,
    u"HEBERGER,ANIMAL"        :    0,
    u"HEBERGER,PARC"          :    0,
    u"HEBERGER,DATEHEURE"     :    0,
    u"SPECIALISER,ESPECE"     :    0,
    u"SPECIALISER,VETERINAIRE":    0,
    u"PROVENIR,PAYS"          :    0,
    u"PROVENIR,ANIMAL"        :    0,
    u"DF2,PAYS"               :    0,
    u"DF2,CONTINENT"          :    0,
    u"DESCENDRE,ANIMAL,-1.0"  :    0,
    u"DESCENDRE,ANIMAL,1.0"   :    0,
}
ratio = {
    u"DF1,ESPECE"   :  1.00,
    u"DF2,CONTINENT":  1.00,
}
colors = {
    u"annotation_color"                : '#000000',
    u"annotation_text_color"           : '#FFFFFF',
    u"association_attribute_text_color": '#000000',
    u"association_cartouche_color"     : '#FFFFFF',
    u"association_cartouche_text_color": '#000000',
    u"association_color"               : '#FFFFFF',
    u"association_stroke_color"        : '#000000',
    u"background_color"                : 'none',
    u"card_text_color"                 : '#000000',
    u"entity_attribute_text_color"     : '#000000',
    u"entity_cartouche_color"          : '#FFFFFF',
    u"entity_cartouche_text_color"     : '#000000',
    u"entity_color"                    : '#FFFFFF',
    u"entity_stroke_color"             : '#000000',
    u"label_text_color"                : '#000000',
    u"leg_stroke_color"                : '#000000',
    u"transparent_color"               : 'none',
}
card_max_width = 22
card_max_height = 15
card_margin = 5
arrow_width = 12
arrow_half_height = 6
arrow_axis = 8
card_baseline = 3

def cmp(x, y):
    return (x > y) - (x < y)

def offset(x, y):
    return (x + card_margin, y - card_baseline - card_margin)

def line_intersection(ex, ey, w, h, ax, ay):
    if ax == ex:
        return (ax, ey + cmp(ay, ey) * h)
    if ay == ey:
        return (ex + cmp(ax, ex) * w, ay)
    x = ex + cmp(ax, ex) * w
    y = ey + (ay-ey) * (x-ex) / (ax-ex)
    if abs(y-ey) > h:
        y = ey + cmp(ay, ey) * h
        x = ex + (ax-ex) * (y-ey) / (ay-ey)
    return (x, y)

def straight_leg_factory(ex, ey, ew, eh, ax, ay, aw, ah, cw, ch):
    
    def card_pos(twist, shift):
        compare = (lambda x1_y1: x1_y1[0] < x1_y1[1]) if twist else (lambda x1_y1: x1_y1[0] <= x1_y1[1])
        diagonal = hypot(ax-ex, ay-ey)
        correction = card_margin * 1.4142 * (1 - abs(abs(ax-ex) - abs(ay-ey)) / diagonal) - shift
        (xg, yg) = line_intersection(ex, ey, ew, eh + ch, ax, ay)
        (xb, yb) = line_intersection(ex, ey, ew + cw, eh, ax, ay)
        if compare((xg, xb)):
            if compare((xg, ex)):
                if compare((yb, ey)):
                    return (xb - correction, yb)
                return (xb - correction, yb + ch)
            if compare((yb, ey)):
                return (xg, yg + ch - correction)
            return (xg, yg + correction)
        if compare((xb, ex)):
            if compare((yb, ey)):
                return (xg - cw, yg + ch - correction)
            return (xg - cw, yg + correction)
        if compare((yb, ey)):
            return (xb - cw + correction, yb)
        return (xb - cw + correction, yb + ch)
    
    def arrow_pos(direction, ratio):
        (x0, y0) = line_intersection(ex, ey, ew, eh, ax, ay)
        (x1, y1) = line_intersection(ax, ay, aw, ah, ex, ey)
        if direction == "<":
            (x0, y0, x1, y1) = (x1, y1, x0, y0)
        (x, y) = (ratio * x0 + (1 - ratio) * x1, ratio * y0 + (1 - ratio) * y1)
        return (x, y, x1 - x0, y0 - y1)
    
    straight_leg_factory.card_pos = card_pos
    straight_leg_factory.arrow_pos = arrow_pos
    return straight_leg_factory


def curved_leg_factory(ex, ey, ew, eh, ax, ay, aw, ah, cw, ch, spin):
    
    def bisection(predicate):
        (a, b) = (0, 1)
        while abs(b - a) > 0.0001:
            m = (a + b) / 2
            if predicate(bezier(m)):
                a = m
            else:
                b = m
        return m
    
    def intersection(left, top, right, bottom):
       (x, y) = bezier(bisection(lambda p: left <= p[0] <= right and top <= p[1] <= bottom))
       return (int(round(x)), int(round(y)))
    
    def card_pos(shift):
        diagonal = hypot(ax-ex, ay-ey)
        correction = card_margin * 1.4142 * (1 - abs(abs(ax-ex) - abs(ay-ey)) / diagonal)
        (top, bot) = (ey - eh, ey + eh)
        (TOP, BOT) = (top - ch, bot + ch)
        (lef, rig) = (ex - ew, ex + ew)
        (LEF, RIG) = (lef - cw, rig + cw)
        (xr, yr) = intersection(LEF, TOP, RIG, BOT)
        (xg, yg) = intersection(lef, TOP, rig, BOT)
        (xb, yb) = intersection(LEF, top, RIG, bot)
        if spin > 0:
            if (yr == BOT and xr <= rig) or (xr == LEF and yr >= bot):
                return (max(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y >= bot) - correction + shift, bot + ch)
            if (xr == RIG and yr >= top) or yr == BOT:
                return (rig, min(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x >= rig) + correction + shift)
            if (yr == TOP and xr >= lef) or xr == RIG:
                return (min(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y <= top) + correction + shift - cw, TOP + ch)
            return (LEF, max(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x <= lef) - correction + shift + ch)
        if (yr == BOT and xr >= lef) or (xr == RIG and yr >= bot):
            return (min(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y >= bot) + correction + shift - cw, bot + ch)
        if xr == RIG or (yr == TOP and xr >= rig):
            return (rig, max(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x >= rig) - correction + shift + ch)
        if yr == TOP or (xr == LEF and yr <= top):
            return (max(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y <= top) - correction + shift, TOP + ch)
        return (LEF, min(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x <= lef) + correction + shift)
    
    def arrow_pos(direction, ratio):
        t0 = bisection(lambda p: abs(p[0] - ax) > aw or abs(p[1] - ay) > ah)
        t3 = bisection(lambda p: abs(p[0] - ex) < ew and abs(p[1] - ey) < eh)
        if direction == "<":
            (t0, t3) = (t3, t0)
        tc = t0 + (t3 - t0) * ratio
        (xc, yc) = bezier(tc)
        (x, y) = derivate(tc)
        if direction == "<":
            (x, y) = (-x, -y)
        return (xc, yc, x, -y)
    
    diagonal = hypot(ax - ex, ay - ey)
    (x, y) = line_intersection(ex, ey, ew + cw / 2, eh + ch / 2, ax, ay)
    k = (cw *  abs((ay - ey) / diagonal) + ch * abs((ax - ex) / diagonal))
    (x, y) = (x - spin * k * (ay - ey) / diagonal, y + spin * k * (ax - ex) / diagonal)
    (hx, hy) = (2 * x - (ex + ax) / 2, 2 * y - (ey + ay) / 2)
    (x1, y1) = (ex + (hx - ex) * 2 / 3, ey + (hy - ey) * 2 / 3)
    (x2, y2) = (ax + (hx - ax) * 2 / 3, ay + (hy - ay) * 2 / 3)
    (kax, kay) = (ex - 2 * hx + ax, ey - 2 * hy + ay)
    (kbx, kby) = (2 * hx - 2 * ex, 2 * hy - 2 * ey)
    bezier = lambda t: (kax*t*t + kbx*t + ex, kay*t*t + kby*t + ey)
    derivate = lambda t: (2*kax*t + kbx, 2*kay*t + kby)
    
    curved_leg_factory.points = (ex, ey, x1, y1, x2, y2, ax, ay)
    curved_leg_factory.card_pos = card_pos
    curved_leg_factory.arrow_pos = arrow_pos
    return curved_leg_factory


def upper_round_rect(x, y, w, h, r):
    return " ".join([str(x) for x in ["M", x + w - r, y, "a", r, r, 90, 0, 1, r, r, "V", y + h, "h", -w, "V", y + r, "a", r, r, 90, 0, 1, r, -r]])

def lower_round_rect(x, y, w, h, r):
    return " ".join([str(x) for x in ["M", x + w, y, "v", h - r, "a", r, r, 90, 0, 1, -r, r, "H", x + r, "a", r, r, 90, 0, 1, -r, -r, "V", y, "H", w]])

def arrow(x, y, a, b):
    c = hypot(a, b)
    (cos, sin) = (a / c, b / c)
    return " ".join([str(x) for x in [ "M", x, y, "L", x + arrow_width * cos - arrow_half_height * sin, y - arrow_half_height * cos - arrow_width * sin, "L", x + arrow_axis * cos, y - arrow_axis * sin, "L", x + arrow_width * cos + arrow_half_height * sin, y + arrow_half_height * cos - arrow_width * sin, "Z"]])

def safe_print_for_PHP(s):
    try:
        print(s)
    except UnicodeEncodeError:
        print(s.encode("utf8"))


lines = '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
lines += '\n\n<svg width="%s" height="%s" view_box="0 0 %s %s"\nxmlns="http://www.w3.org/2000/svg"\nxmlns:link="http://www.w3.org/1999/xlink">' % (width,height,width,height)
lines += u'\\n\\n<desc>Généré par Mocodo 2.3.8 le %s</desc>' % time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
lines += '\n\n<rect id="frame" x="0" y="0" width="%s" height="%s" fill="%s" stroke="none" stroke-width="0"/>' % (width,height,colors['background_color'] if colors['background_color'] else "none")

lines += u"""\n\n<!-- Association VERSER -->"""
(x,y) = (cx[u"VERSER"],cy[u"VERSER"])
(ex,ey) = (cx[u"MEMBRE"],cy[u"MEMBRE"])
leg=straight_leg_factory(ex,ey,61,53,x,y,55,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"VERSER,MEMBRE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"DATEHEURE"],cy[u"DATEHEURE"])
leg=straight_leg_factory(ex,ey,46,26,x,y,55,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(True,shift[u"VERSER,DATEHEURE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-VERSER">""" % {}
path = upper_round_rect(-55+x,-26+y,110,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-55+x,0.0+y,110,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="110" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -55+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -55+x, 'y0': 0+y, 'x1': 55+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">VERSER</text>""" % {'x': -24+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">somme_versee</text>""" % {'x': -48+x, 'y': 18.6+y, 'text_color': colors['association_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association RECENSER -->"""
(x,y) = (cx[u"RECENSER"],cy[u"RECENSER"])
(ex,ey) = (cx[u"ESPECE"],cy[u"ESPECE"])
leg=straight_leg_factory(ex,ey,44,44,x,y,46,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(True,shift[u"RECENSER,ESPECE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"DATEHEURE"],cy[u"DATEHEURE"])
leg=straight_leg_factory(ex,ey,46,26,x,y,46,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"RECENSER,DATEHEURE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-RECENSER">""" % {}
path = upper_round_rect(-46+x,-26+y,92,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-46+x,0.0+y,92,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="92" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -46+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -46+x, 'y0': 0+y, 'x1': 46+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">RECENSER</text>""" % {'x': -33+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nb_animaux</text>""" % {'x': -39+x, 'y': 18.6+y, 'text_color': colors['association_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association VIVRE_LIBRE -->"""
(x,y) = (cx[u"VIVRE_LIBRE"],cy[u"VIVRE_LIBRE"])
(ex,ey) = (cx[u"PAYS"],cy[u"PAYS"])
leg=straight_leg_factory(ex,ey,37,35,x,y,48,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"VIVRE_LIBRE,PAYS"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"ESPECE"],cy[u"ESPECE"])
leg=straight_leg_factory(ex,ey,44,44,x,y,48,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"VIVRE_LIBRE,ESPECE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-VIVRE_LIBRE">""" % {}
path = upper_round_rect(-48+x,-26+y,96,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-48+x,0.0+y,96,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="96" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -48+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -48+x, 'y0': 0+y, 'x1': 48+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">VIVRE_LIBRE</text>""" % {'x': -41+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association VISITER -->"""
(x,y) = (cx[u"VISITER"],cy[u"VISITER"])
(ex,ey) = (cx[u"VETERINAIRE"],cy[u"VETERINAIRE"])
leg=straight_leg_factory(ex,ey,50,71,x,y,54,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"VISITER,VETERINAIRE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"ANIMAL"],cy[u"ANIMAL"])
leg=straight_leg_factory(ex,ey,55,71,x,y,54,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"VISITER,ANIMAL"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"DATEHEURE"],cy[u"DATEHEURE"])
leg=straight_leg_factory(ex,ey,46,26,x,y,54,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"VISITER,DATEHEURE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-VISITER">""" % {}
path = upper_round_rect(-54+x,-26+y,108,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-54+x,0.0+y,108,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="108" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -54+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -54+x, 'y0': 0+y, 'x1': 54+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">VISITER</text>""" % {'x': -25+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">bulletin_visite</text>""" % {'x': -47+x, 'y': 18.6+y, 'text_color': colors['association_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association DF1 -->"""
(x,y) = (cx[u"DF1"],cy[u"DF1"])
(ex,ey) = (cx[u"ANIMAL"],cy[u"ANIMAL"])
leg=straight_leg_factory(ex,ey,55,71,x,y,16,16,21+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"DF1,ANIMAL"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ux,uy)=(tx+21,ty--2)
lines += u"""\n<line x1="%(tx)s" y1="%(uy)s" x2="%(ux)s" y2="%(uy)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'tx': tx, 'uy': uy, 'ux': ux, 'uy': uy, 'stroke_color': colors['card_text_color']}
(ex,ey) = (cx[u"ESPECE"],cy[u"ESPECE"])
leg=straight_leg_factory(ex,ey,44,44,x,y,16,16,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"DF1,ESPECE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"DF1,ESPECE"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-DF1">""" % {}
lines += u"""\n	<circle cx="%(cx)s" cy="%(cy)s" r="16" stroke="%(stroke_color)s" stroke-width="1.5" fill="%(color)s"/>""" % {'cx': x, 'cy': y, 'stroke_color': colors['association_stroke_color'], 'color': colors['association_cartouche_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">DF</text>""" % {'x': -9+x, 'y': 3.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association CONTROLER -->"""
(x,y) = (cx[u"CONTROLER"],cy[u"CONTROLER"])
(ex,ey) = (cx[u"CONTROLEUR"],cy[u"CONTROLEUR"])
leg=straight_leg_factory(ex,ey,68,62,x,y,54,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"CONTROLER,CONTROLEUR"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"PARC"],cy[u"PARC"])
leg=straight_leg_factory(ex,ey,45,80,x,y,54,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"CONTROLER,PARC"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"DATEHEURE"],cy[u"DATEHEURE"])
leg=straight_leg_factory(ex,ey,46,26,x,y,54,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(True,shift[u"CONTROLER,DATEHEURE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-CONTROLER">""" % {}
path = upper_round_rect(-54+x,-26+y,108,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-54+x,0.0+y,108,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="108" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -54+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -54+x, 'y0': 0+y, 'x1': 54+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">CONTROLER</text>""" % {'x': -39+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">compte_rendu</text>""" % {'x': -47+x, 'y': 18.6+y, 'text_color': colors['association_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association HEBERGER -->"""
(x,y) = (cx[u"HEBERGER"],cy[u"HEBERGER"])
(ex,ey) = (cx[u"ANIMAL"],cy[u"ANIMAL"])
leg=straight_leg_factory(ex,ey,55,71,x,y,58,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"HEBERGER,ANIMAL"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"PARC"],cy[u"PARC"])
leg=straight_leg_factory(ex,ey,45,80,x,y,58,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"HEBERGER,PARC"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"DATEHEURE"],cy[u"DATEHEURE"])
leg=straight_leg_factory(ex,ey,46,26,x,y,58,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"HEBERGER,DATEHEURE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-HEBERGER">""" % {}
path = upper_round_rect(-58+x,-26+y,116,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-58+x,0.0+y,116,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="116" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -58+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -58+x, 'y0': 0+y, 'x1': 58+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">HEBERGER</text>""" % {'x': -34+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">motif_presence</text>""" % {'x': -51+x, 'y': 18.6+y, 'text_color': colors['association_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association SPECIALISER -->"""
(x,y) = (cx[u"SPECIALISER"],cy[u"SPECIALISER"])
(ex,ey) = (cx[u"ESPECE"],cy[u"ESPECE"])
leg=straight_leg_factory(ex,ey,44,44,x,y,47,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"SPECIALISER,ESPECE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"VETERINAIRE"],cy[u"VETERINAIRE"])
leg=straight_leg_factory(ex,ey,50,71,x,y,47,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"SPECIALISER,VETERINAIRE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-SPECIALISER">""" % {}
path = upper_round_rect(-47+x,-26+y,94,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-47+x,0.0+y,94,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="94" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -47+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -47+x, 'y0': 0+y, 'x1': 47+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">SPECIALISER</text>""" % {'x': -40+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association PROVENIR -->"""
(x,y) = (cx[u"PROVENIR"],cy[u"PROVENIR"])
(ex,ey) = (cx[u"PAYS"],cy[u"PAYS"])
leg=straight_leg_factory(ex,ey,37,35,x,y,40,26,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"PROVENIR,PAYS"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"ANIMAL"],cy[u"ANIMAL"])
leg=straight_leg_factory(ex,ey,55,71,x,y,40,26,21+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"PROVENIR,ANIMAL"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-PROVENIR">""" % {}
path = upper_round_rect(-40+x,-26+y,80,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-40+x,0.0+y,80,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="80" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -40+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -40+x, 'y0': 0+y, 'x1': 40+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">PROVENIR</text>""" % {'x': -33+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association DF2 -->"""
(x,y) = (cx[u"DF2"],cy[u"DF2"])
(ex,ey) = (cx[u"PAYS"],cy[u"PAYS"])
leg=straight_leg_factory(ex,ey,37,35,x,y,16,16,21+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"DF2,PAYS"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ux,uy)=(tx+21,ty--2)
lines += u"""\n<line x1="%(tx)s" y1="%(uy)s" x2="%(ux)s" y2="%(uy)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'tx': tx, 'uy': uy, 'ux': ux, 'uy': uy, 'stroke_color': colors['card_text_color']}
(ex,ey) = (cx[u"CONTINENT"],cy[u"CONTINENT"])
leg=straight_leg_factory(ex,ey,54,35,x,y,16,16,22+2*card_margin,15+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"DF2,CONTINENT"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"DF2,CONTINENT"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-DF2">""" % {}
lines += u"""\n	<circle cx="%(cx)s" cy="%(cy)s" r="16" stroke="%(stroke_color)s" stroke-width="1.5" fill="%(color)s"/>""" % {'cx': x, 'cy': y, 'stroke_color': colors['association_stroke_color'], 'color': colors['association_cartouche_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">DF</text>""" % {'x': -9+x, 'y': 3.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association DESCENDRE -->"""
(x,y) = (cx[u"DESCENDRE"],cy[u"DESCENDRE"])
(ex,ey) = (cx[u"ANIMAL"],cy[u"ANIMAL"])
leg=curved_leg_factory(ex,ey,55,71,x,y,45,26,21+2*card_margin,15+2*card_margin,-1.0)
(x0, y0, x1, y1, x2, y2, x3, y3)=leg.points
lines += u"""\n<path d="M%(x0)s %(y0)s C %(x1)s %(y1)s %(x2)s %(y2)s %(x3)s %(y3)s" fill="none" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'x3': x3, 'y3': y3, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(shift[u"DESCENDRE,ANIMAL,-1.0"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,2</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"ANIMAL"],cy[u"ANIMAL"])
leg=curved_leg_factory(ex,ey,55,71,x,y,45,26,22+2*card_margin,15+2*card_margin,1.0)
(x0, y0, x1, y1, x2, y2, x3, y3)=leg.points
lines += u"""\n<path d="M%(x0)s %(y0)s C %(x1)s %(y1)s %(x2)s %(y2)s %(x3)s %(y3)s" fill="none" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'x3': x3, 'y3': y3, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(shift[u"DESCENDRE,ANIMAL,1.0"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-DESCENDRE">""" % {}
path = upper_round_rect(-45+x,-26+y,90,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-45+x,0.0+y,90,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="90" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -45+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -45+x, 'y0': 0+y, 'x1': 45+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">DESCENDRE</text>""" % {'x': -38+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity MEMBRE -->"""
(x,y) = (cx[u"MEMBRE"],cy[u"MEMBRE"])
lines += u"""\n<g id="entity-MEMBRE">""" % {}
lines += u"""\n	<g id="frame-MEMBRE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="122" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -61+x, 'y': -53+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="122" height="80" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -61+x, 'y': -27.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="122" height="106" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -61+x, 'y': -53+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -61+x, 'y0': -27+y, 'x1': 61+x, 'y1': -27+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">MEMBRE</text>""" % {'x': -27+x, 'y': -34.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">id_membre</text>""" % {'x': -56+x, 'y': -8.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -56+x, 'y0': -6.0+y, 'x1': 18+x, 'y1': -6.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom_membre</text>""" % {'x': -56+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">prenom_membre</text>""" % {'x': -56+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">adr_membre</text>""" % {'x': -56+x, 'y': 45.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity ESPECE -->"""
(x,y) = (cx[u"ESPECE"],cy[u"ESPECE"])
lines += u"""\n<g id="entity-ESPECE">""" % {}
lines += u"""\n	<g id="frame-ESPECE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="88" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -44+x, 'y': -44+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="88" height="62" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -44+x, 'y': -18.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="88" height="88" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -44+x, 'y': -44+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -44+x, 'y0': -18+y, 'x1': 44+x, 'y1': -18+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">ESPECE</text>""" % {'x': -24+x, 'y': -25.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">id_espece</text>""" % {'x': -39+x, 'y': 0.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -39+x, 'y0': 3.0+y, 'x1': 26+x, 'y1': 3.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom espece</text>""" % {'x': -39+x, 'y': 18.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nb_monde</text>""" % {'x': -39+x, 'y': 36.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity DATEHEURE -->"""
(x,y) = (cx[u"DATEHEURE"],cy[u"DATEHEURE"])
lines += u"""\n<g id="entity-DATEHEURE">""" % {}
lines += u"""\n	<g id="frame-DATEHEURE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="92" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -46+x, 'y': -26+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="92" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -46+x, 'y': 0.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="92" height="52" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -46+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -46+x, 'y0': 0+y, 'x1': 46+x, 'y1': 0+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">DATEHEURE</text>""" % {'x': -39+x, 'y': -7.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">jj/mm/aaaa</text>""" % {'x': -41+x, 'y': 18.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -41+x, 'y0': 21.0+y, 'x1': 40+x, 'y1': 21.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity VETERINAIRE -->"""
(x,y) = (cx[u"VETERINAIRE"],cy[u"VETERINAIRE"])
lines += u"""\n<g id="entity-VETERINAIRE">""" % {}
lines += u"""\n	<g id="frame-VETERINAIRE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="100" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -50+x, 'y': -71+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="100" height="116" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -50+x, 'y': -45.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="100" height="142" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -50+x, 'y': -71+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -50+x, 'y0': -45+y, 'x1': 50+x, 'y1': -45+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">VETERINAIRE</text>""" % {'x': -42+x, 'y': -52.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">id_veto</text>""" % {'x': -45+x, 'y': -26.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -45+x, 'y0': -24.0+y, 'x1': 4+x, 'y1': -24.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom_veto</text>""" % {'x': -45+x, 'y': -8.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">prenom_veto</text>""" % {'x': -45+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">adr_veto</text>""" % {'x': -45+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">tel_veto</text>""" % {'x': -45+x, 'y': 45.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">tel_port_veto</text>""" % {'x': -45+x, 'y': 63.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity PAYS -->"""
(x,y) = (cx[u"PAYS"],cy[u"PAYS"])
lines += u"""\n<g id="entity-PAYS">""" % {}
lines += u"""\n	<g id="frame-PAYS">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="74" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -37+x, 'y': -35+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="74" height="44" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -37+x, 'y': -9.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="74" height="70" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -37+x, 'y': -35+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -37+x, 'y0': -9+y, 'x1': 37+x, 'y1': -9+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">PAYS</text>""" % {'x': -17+x, 'y': -16.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">id_pays</text>""" % {'x': -32+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y)s" x2="%(x1)s" y2="%(y)s" style="fill:none;stroke:%(stroke_color)s;stroke-width:1;stroke-dasharray:4;"/>""" % {'x0': -32+x, 'y': 12.0+y, 'x1': 17+x, 'y': 12.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom_pays</text>""" % {'x': -32+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity CONTROLEUR -->"""
(x,y) = (cx[u"CONTROLEUR"],cy[u"CONTROLEUR"])
lines += u"""\n<g id="entity-CONTROLEUR">""" % {}
lines += u"""\n	<g id="frame-CONTROLEUR">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="136" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -68+x, 'y': -62+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="136" height="98" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -68+x, 'y': -36.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="136" height="124" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -68+x, 'y': -62+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -68+x, 'y0': -36+y, 'x1': 68+x, 'y1': -36+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">CONTROLEUR</text>""" % {'x': -44+x, 'y': -43.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">id_controleur</text>""" % {'x': -63+x, 'y': -17.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -63+x, 'y0': -15.0+y, 'x1': 25+x, 'y1': -15.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom_controleur</text>""" % {'x': -63+x, 'y': 0.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">prenom_controleur</text>""" % {'x': -63+x, 'y': 18.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">adr_controleur</text>""" % {'x': -63+x, 'y': 36.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">tel_controleur</text>""" % {'x': -63+x, 'y': 54.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity PARC -->"""
(x,y) = (cx[u"PARC"],cy[u"PARC"])
lines += u"""\n<g id="entity-PARC">""" % {}
lines += u"""\n	<g id="frame-PARC">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="90" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -45+x, 'y': -80+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="90" height="134" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -45+x, 'y': -54.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="90" height="160" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -45+x, 'y': -80+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -45+x, 'y0': -54+y, 'x1': 45+x, 'y1': -54+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">PARC</text>""" % {'x': -17+x, 'y': -61.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">id_parc</text>""" % {'x': -40+x, 'y': -35.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -40+x, 'y0': -33.0+y, 'x1': 9+x, 'y1': -33.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom_parc</text>""" % {'x': -40+x, 'y': -17.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">adr_parc</text>""" % {'x': -40+x, 'y': 0.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">tel_parc</text>""" % {'x': -40+x, 'y': 18.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">superficie</text>""" % {'x': -40+x, 'y': 36.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">date_entree</text>""" % {'x': -40+x, 'y': 54.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">date_exclu</text>""" % {'x': -40+x, 'y': 72.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity ANIMAL -->"""
(x,y) = (cx[u"ANIMAL"],cy[u"ANIMAL"])
lines += u"""\n<g id="entity-ANIMAL">""" % {}
lines += u"""\n	<g id="frame-ANIMAL">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="110" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -55+x, 'y': -71+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="110" height="116" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -55+x, 'y': -45.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="110" height="142" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -55+x, 'y': -71+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -55+x, 'y0': -45+y, 'x1': 55+x, 'y1': -45+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">ANIMAL</text>""" % {'x': -25+x, 'y': -52.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">ref_animal</text>""" % {'x': -50+x, 'y': -26.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y)s" x2="%(x1)s" y2="%(y)s" style="fill:none;stroke:%(stroke_color)s;stroke-width:1;stroke-dasharray:4;"/>""" % {'x0': -50+x, 'y': -24.0+y, 'x1': 21+x, 'y': -24.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom_animal</text>""" % {'x': -50+x, 'y': -8.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">sexe</text>""" % {'x': -50+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">date_naissance</text>""" % {'x': -50+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">date_deces</text>""" % {'x': -50+x, 'y': 45.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">cause_deces</text>""" % {'x': -50+x, 'y': 63.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity CONTINENT -->"""
(x,y) = (cx[u"CONTINENT"],cy[u"CONTINENT"])
lines += u"""\n<g id="entity-CONTINENT">""" % {}
lines += u"""\n	<g id="frame-CONTINENT">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="108" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -54+x, 'y': -35+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="108" height="44" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -54+x, 'y': -9.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="108" height="70" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -54+x, 'y': -35+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -54+x, 'y0': -9+y, 'x1': 54+x, 'y1': -9+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">CONTINENT</text>""" % {'x': -38+x, 'y': -16.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">id_continent</text>""" % {'x': -49+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -49+x, 'y0': 12.0+y, 'x1': 33+x, 'y1': 12.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Trebuchet MS" font-size="14">nom_continent</text>""" % {'x': -49+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}
lines += u'\n</svg>'

with codecs.open(r"mocodo_notebook\sandbox.svg", "w", "utf8") as f:
    f.write(lines)
safe_print_for_PHP(u'Fichier de sortie "mocodo_notebook\sandbox.svg" généré avec succès.')