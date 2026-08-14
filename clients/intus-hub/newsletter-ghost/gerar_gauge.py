#!/usr/bin/env python3
"""
Gerador de Fear & Greed Gauge — Intus Cripto
Paleta: Azul marinho escuro + Dourado
"""
import sys
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc, Wedge
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

# ── Paleta Intus Cripto ─────────────────────────────────────────────────────
BG_COLOR      = '#0a1628'   # Azul marinho escuro
GOLD          = '#c9a020'   # Dourado principal
GOLD_LIGHT    = '#f0c040'   # Dourado claro (highlights)
BLUE_GLOW     = '#1a5fd6'   # Azul elétrico
WHITE         = '#ffffff'
GRAY_LIGHT    = '#a0b0c8'

# ── Cores do gauge (vermelho → amarelo → verde) ─────────────────────────────
GAUGE_COLORS = [
    (0,   '#c0392b'),   # Extreme Fear
    (25,  '#e67e22'),   # Fear
    (45,  '#f1c40f'),   # Neutral
    (60,  '#2ecc71'),   # Greed
    (80,  '#27ae60'),   # Extreme Greed
    (100, '#1a8a4a'),
]


def interpolate_color(value):
    """Retorna cor hex baseada no valor 0-100."""
    for i in range(len(GAUGE_COLORS) - 1):
        v0, c0 = GAUGE_COLORS[i]
        v1, c1 = GAUGE_COLORS[i + 1]
        if v0 <= value <= v1:
            t = (value - v0) / (v1 - v0)
            r0, g0, b0 = int(c0[1:3], 16), int(c0[3:5], 16), int(c0[5:7], 16)
            r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
            r = int(r0 + t * (r1 - r0))
            g = int(g0 + t * (g1 - g0))
            b = int(b0 + t * (b1 - b0))
            return f'#{r:02x}{g:02x}{b:02x}'
    return GAUGE_COLORS[-1][1]


def get_label(value):
    if value <= 24:  return 'Extreme Fear'
    if value <= 44:  return 'Fear'
    if value <= 55:  return 'Neutral'
    if value <= 74:  return 'Greed'
    return 'Extreme Greed'


def gerar_gauge(valor=33, ontem=25, semana_passada=45,
                output_path='fear_greed_gauge.png'):

    label = get_label(valor)
    needle_color = interpolate_color(valor)

    fig, ax = plt.subplots(figsize=(6, 4.6), facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-0.80, 1.25)
    ax.set_aspect('equal')
    ax.axis('off')

    # ── Título ──────────────────────────────────────────────────────────────
    ax.text(0, 1.18, 'Fear & Greed Index',
            ha='center', va='top', fontsize=13, fontweight='bold',
            color=GOLD, fontfamily='DejaVu Sans')

    ax.text(0, 1.05, 'Intus Cripto — Sentimento do Mercado',
            ha='center', va='top', fontsize=7.5, color=GRAY_LIGHT)

    # ── Linha separadora dourada ─────────────────────────────────────────────
    ax.plot([-1.1, 1.1], [0.96, 0.96], color=GOLD, linewidth=0.8, alpha=0.5)

    # ── Arco de fundo (cinza escuro) ─────────────────────────────────────────
    n_segments = 200
    for i in range(n_segments):
        angle_start = 180 - (i / n_segments) * 180
        angle_end   = 180 - ((i + 1) / n_segments) * 180
        seg_value   = (i / n_segments) * 100
        color       = interpolate_color(seg_value)
        wedge = Wedge((0, 0), 0.90, angle_end, angle_start,
                      width=0.22, facecolor=color, edgecolor='none', alpha=0.90)
        ax.add_patch(wedge)

    # ── Borda interna e externa dourada ──────────────────────────────────────
    outer = plt.Circle((0, 0), 0.92, fill=False, edgecolor=GOLD, linewidth=1.2, alpha=0.6)
    inner = plt.Circle((0, 0), 0.67, fill=False, edgecolor=GOLD, linewidth=0.8, alpha=0.4)
    ax.add_patch(outer)
    ax.add_patch(inner)

    # ── Marcadores de escala ─────────────────────────────────────────────────
    for tick_val in [0, 25, 50, 75, 100]:
        angle_deg = 180 - (tick_val / 100) * 180
        angle_rad = math.radians(angle_deg)
        x0 = 0.68 * math.cos(angle_rad)
        y0 = 0.68 * math.sin(angle_rad)
        x1 = 0.92 * math.cos(angle_rad)
        y1 = 0.92 * math.sin(angle_rad)
        ax.plot([x0, x1], [y0, y1], color=WHITE, linewidth=1.0, alpha=0.7)
        xt = 1.02 * math.cos(angle_rad)
        yt = 1.02 * math.sin(angle_rad)
        ax.text(xt, yt, str(tick_val), ha='center', va='center',
                fontsize=6.5, color=GRAY_LIGHT)

    # ── Agulha ───────────────────────────────────────────────────────────────
    needle_angle_deg = 180 - (valor / 100) * 180
    needle_angle_rad = math.radians(needle_angle_deg)
    nx = 0.75 * math.cos(needle_angle_rad)
    ny = 0.75 * math.sin(needle_angle_rad)
    ax.annotate('', xy=(nx, ny), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=WHITE,
                                lw=2.5, mutation_scale=12))

    # ── Centro da agulha ─────────────────────────────────────────────────────
    center_outer = plt.Circle((0, 0), 0.075, facecolor=GOLD, edgecolor=GOLD_LIGHT, linewidth=1.5, zorder=5)
    center_inner = plt.Circle((0, 0), 0.035, facecolor=BG_COLOR, edgecolor='none', zorder=6)
    ax.add_patch(center_outer)
    ax.add_patch(center_inner)

    # ── Valor principal (abaixo do pivot, sem sobreposição) ───────────────────
    ax.text(0, -0.20, str(valor),
            ha='center', va='center', fontsize=38, fontweight='bold',
            color=WHITE, fontfamily='DejaVu Sans', zorder=7)

    ax.text(0, -0.42, label,
            ha='center', va='center', fontsize=13, fontweight='bold',
            color=needle_color)

    # ── Linha separadora ─────────────────────────────────────────────────────
    ax.plot([-1.1, 1.1], [-0.54, -0.54], color=GOLD, linewidth=0.6, alpha=0.35)

    # ── Ontem e Semana Passada ────────────────────────────────────────────────
    ax.text(-0.55, -0.60, 'Ontem', ha='center', fontsize=7.5, color=GRAY_LIGHT)
    ax.text(-0.55, -0.66, get_label(ontem), ha='center', fontsize=7, color=interpolate_color(ontem))
    ax.text(-0.55, -0.73, str(ontem), ha='center', fontsize=11, fontweight='bold', color=WHITE)

    ax.text(0.55, -0.60, 'Semana passada', ha='center', fontsize=7.5, color=GRAY_LIGHT)
    ax.text(0.55, -0.66, get_label(semana_passada), ha='center', fontsize=7, color=interpolate_color(semana_passada))
    ax.text(0.55, -0.73, str(semana_passada), ha='center', fontsize=11, fontweight='bold', color=WHITE)

    # ── Borda externa da figura ───────────────────────────────────────────────
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(False)

    fig.tight_layout(pad=0.3)
    fig.savefig(output_path, dpi=150, bbox_inches='tight',
                facecolor=BG_COLOR, edgecolor='none')
    plt.close(fig)
    print(f'Gauge salvo: {output_path}')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--valor',   type=int, default=33)
    parser.add_argument('--ontem',   type=int, default=25)
    parser.add_argument('--semana',  type=int, default=45)
    parser.add_argument('--output',  default='fear_greed_gauge.png')
    args = parser.parse_args()
    gerar_gauge(args.valor, args.ontem, args.semana, args.output)
