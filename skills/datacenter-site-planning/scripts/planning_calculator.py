"""Unit-explicit concept arithmetic; no compliance or engineering certification."""
import argparse
import json
import math


def positive(value):
    x = float(value)
    if not math.isfinite(x) or x <= 0:
        raise argparse.ArgumentTypeError('must be finite and positive')
    return x


def ratio(value):
    x = positive(value)
    if x > 1:
        raise argparse.ArgumentTypeError('must be a fraction in (0, 1]')
    return x


def capacity(area_ha, far, nta_ratio, density_kw_m2):
    gfa = area_ha * 10000 * far
    nta = gfa * nta_ratio
    return dict(gfa_m2=gfa, nta_m2=nta, it_mw=nta*density_kw_m2/1000)


def cooling(it_mw, thermal_factor, kw_per_tr, auxiliary_factor):
    q = it_mw * thermal_factor
    tr = q * 1000 / 3.51685284
    chiller = tr * kw_per_tr / 1000
    return dict(thermal_mwc=q, refrigeration_tr=tr, chiller_mwe=chiller,
                cooling_mwe=chiller*auxiliary_factor)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='mode', required=True)
    c = sub.add_parser('capacity')
    for key in ['area-ha', 'far', 'density-kw-m2']:
        c.add_argument('--'+key, type=positive, required=True)
    c.add_argument('--nta-ratio', type=ratio, required=True)
    q = sub.add_parser('cooling')
    for key in ['it-mw', 'thermal-factor', 'kw-per-tr', 'auxiliary-factor']:
        q.add_argument('--'+key, type=positive, required=True)
    args = vars(p.parse_args())
    mode = args.pop('mode')
    result = capacity(**args) if mode == 'capacity' else cooling(**args)
    print(json.dumps(dict(status='CONCEPT_ASSUMPTIONS_NOT_DESIGN', inputs=args,
                          results=result), indent=2))


if __name__ == '__main__':
    main()
