# coding: utf-8

#
# This show_receptive_field_width is based on some code of wavenet train.py 
# in <https://github.com/musyoku/wavenet/blob/master/train_audio/train.py>
# by musyoku
#
# example:
# from receptive_field_width import show_receptive_field_width
# show_receptive_field_width(args.n_layer, args.n_loop, residual_conv_filter_width=2, sampling_rate=16000)
#
# In chainer-examples-wavnet, residual_conv_filter_width uses fixed value 2.


def show_receptive_field_width(residual_num_layers, residual_num_blocks, residual_conv_filter_width=2, sampling_rate=16000):
    # receptive width 
    receptive_width_per_unit = residual_conv_filter_width ** residual_num_layers 
    receptive_width = (receptive_width_per_unit - 1) * residual_num_blocks + 1 
    receptive_msec = int(receptive_width * 1000.0 / sampling_rate) 
    
    # receptive field width 
    input_width = receptive_width 
    # padding for causal conv block 
    input_width += 1  # len(params.causal_conv_channels) 
    
    print ('receptive field width ', receptive_width, '  receptive field msec ', receptive_msec, '[mSec]')
