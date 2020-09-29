# python bleu.py --ref exps/ref.txt --hyp exps/hyp.txt

import argparse
import os

from utils import bool_flag, compute_bleu

def get_parser():
    """
    Generate a parameters parser.
    """
    # parse parameters
    parser = argparse.ArgumentParser(description="eval BLEU params")

    # main parameters
    parser.add_argument("--ref", type=str, default="", help="")
    parser.add_argument("--hyp", type=str, default="", help="")
    parser.add_argument("--max_order", type=int, default=4, help="")
    parser.add_argument("--smooth", type=bool_flag, default=False, help="")

    return parser

if __name__ == '__main__':
    # generate parser / parse parameters
    parser = get_parser()
    params = parser.parse_args()

    # check parameters
    assert os.path.isfile(params.ref)
    assert os.path.isfile(params.hyp)

    refs = []
    with open(params.ref) as ref :
        tmp = []
        for line in ref.readlines() :
          if line != "\n" :
            tmp.append(line.strip().split())
          else :
            refs.append(tmp)
            tmp = [] 

    hyps = [line.strip().split() for line in open(params.hyp).readlines()]
    
    r = compute_bleu(reference_corpus = refs, translation_corpus = hyps, max_order = params.max_order, smooth = params.smooth)
    print(r)
    