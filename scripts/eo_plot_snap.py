# from snappy import Product
# from snappy import ProductData
# import snappy
#
# import numpy
# import sys

# from snappy import String

def plot_RGB(basedir):

    from snappy import ProductIO
    from snappy import ProductUtils
    from snappy import ProgressMonitor
    from snappy import jpy

    from os.path import join
    from tempfile import mkstemp

    mtd = 'MTD_MSIL1C.xml'
    _, rgb_image = mkstemp(dir='.', prefix= 'RGB', suffix='.png')
    source = join(basedir, mtd)

    sourceProduct = ProductIO.readProduct(source)
    b2 = sourceProduct.getBand('B2')
    b3 = sourceProduct.getBand('B3')
    b4 = sourceProduct.getBand('B4')

    Color = jpy.get_type('java.awt.Color')
    ColorPoint = jpy.get_type('org.esa.snap.core.datamodel.ColorPaletteDef$Point')
    ColorPaletteDef = jpy.get_type('org.esa.snap.core.datamodel.ColorPaletteDef')
    ImageInfo = jpy.get_type('org.esa.snap.core.datamodel.ImageInfo')
    ImageLegend = jpy.get_type('org.esa.snap.core.datamodel.ImageLegend')
    ImageManager = jpy.get_type('org.esa.snap.core.image.ImageManager')
    JAI = jpy.get_type('javax.media.jai.JAI')
    RenderedImage = jpy.get_type('java.awt.image.RenderedImage')


    # Disable JAI native MediaLib extensions
    System = jpy.get_type('java.lang.System')
    System.setProperty('com.sun.media.jai.disableMediaLib', 'true')

    #
    legend = ImageLegend(b2.getImageInfo(), b2)
    legend.setHeaderText(b2.getName())

    # red = product.getBand('B4')
    # green = product.getBand('B3')
    # blue = product.getBand('B2')

    image_info = ProductUtils.createImageInfo([b4, b3, b2], True, ProgressMonitor.NULL)
    im = ImageManager.getInstance().createColoredBandImage([b4, b3, b2], image_info, 0)
    JAI.create("filestore", im, rgb_image, 'PNG')

    return rgb_image

basedir = '/home/nils/birdhouse/var/lib/pywps/cache/flyingpigeon/scihub.copernicus/S2A_MSIL1C_20170119T092311_N0204_R093_T33PVK_20170119T093234.SAFE/'

plot_RGB(basedir)


#
# source = '/home/nils/birdhouse/var/lib/pywps/cache/flyingpigeon/scihub.copernicus/S2A_MSIL1C_20170119T092311_N0204_R093_T33PVK_20170119T093234.SAFE/MTD_MSIL1C.xml'
# sourceProduct = ProductIO.readProduct(source)
# sourceProduct.getBandNames()
#
# b2 = sourceProduct.getBand('B2')
# b3 = sourceProduct.getBand('B3')
# b4 = sourceProduct.getBand('B4')
# #
# jpy = snappy.jpy
#
# # More Java type definitions required for image generation
# Color = jpy.get_type('java.awt.Color')
# ColorPoint = jpy.get_type('org.esa.snap.core.datamodel.ColorPaletteDef$Point')
# ColorPaletteDef = jpy.get_type('org.esa.snap.core.datamodel.ColorPaletteDef')
# ImageInfo = jpy.get_type('org.esa.snap.core.datamodel.ImageInfo')
# ImageLegend = jpy.get_type('org.esa.snap.core.datamodel.ImageLegend')
# ImageManager = jpy.get_type('org.esa.snap.core.image.ImageManager')
# JAI = jpy.get_type('javax.media.jai.JAI')
# RenderedImage = jpy.get_type('java.awt.image.RenderedImage')
#
# # Disable JAI native MediaLib extensions
# System = jpy.get_type('java.lang.System')
# System.setProperty('com.sun.media.jai.disableMediaLib', 'true')
#
# def write_image(band, filename, format):
#     im = ImageManager.getInstance().createColoredBandImage([band], band.getImageInfo(), 0)
#     JAI.create("filestore", im, filename, format)
#
# def write_rgb_image(bands, filename, format):
#     image_info = ProductUtils.createImageInfo(bands, True, ProgressMonitor.NULL)
#     im = ImageManager.getInstance().createColoredBandImage(bands, image_info, 0)
#     JAI.create("filestore", im, filename, format)
#
# # points = [ColorPoint(0.0, Color.YELLOW),
# #           ColorPoint(50.0, Color.RED),
# #           ColorPoint(100.0, Color.BLUE)]
# # cpd = ColorPaletteDef(points)
# # ii = ImageInfo(cpd)
# # b2.setImageInfo(ii)
# #
# image_format = 'PNG'
#
# # write_image(b2, 'snappy_image.png', image_format)
# # legend_image = legend.createImage()
# #
# # # This cast is need because otherwise jpy can't evaluate which method to call
# # # This is considered as an issue of jpy (https://github.com/bcdev/jpy/issues/89)
# # rendered_legend_image = jpy.cast(legend_image, RenderedImage)
# # JAI.create("filestore", rendered_legend_image, 'snappy_write_image_legend.png', image_format)
# #
# legend = ImageLegend(b2.getImageInfo(), b2)
# legend.setHeaderText(b2.getName())
#
# # red = product.getBand('B4')
# # green = product.getBand('B3')
# # blue = product.getBand('B2')
#
# write_rgb_image([b4, b3, b2], 'snappy_write_image_rgb.png', image_format)
# #
# # #legend.setOrientation(ImageLegend.HORIZONTAL) # or ImageLegend.VERTICAL
# #legend.setFont(legend.getFont().deriveFont(14))
# #legend.setBackgroundColor(Color.CYAN)
# #legend.setForegroundColor(Color.ORANGE);
# #legend.setBackgroundTransparency(0.7);
# #legend.setBackgroundTransparencyEnabled(True);
# #legend.setAntialiasing(True);
#
# legend_image = legend.createImage()
#
# # This cast is need because otherwise jpy can't evaluate which method to call
# # This is considered as an issue of jpy (https://github.com/bcdev/jpy/issues/89)
# rendered_legend_image = jpy.cast(legend_image, RenderedImage)
# JAI.create("filestore", rendered_legend_image, 'snappy_write_image_legend.png', image_format)
#
# red = product.getBand('B4')
# green = product.getBand('B3')
# blue = product.getBand('B2')
# write_rgb_image([red, green, blue], 'snappy_write_image_rgb.png', image_format)
#
# # This cast is need because otherwise jpy can't evaluate which method to call
# # This is considered as an issue of jpy (https://github.com/bcdev/jpy/issues/89)
# rendered_legend_image = jpy.cast(legend_image, RenderedImage)
# JAI.create("filestore", rendered_legend_image, 'snappy_write_image_legend.png', image_format)
#
# red = sourceProduct.getBand('B4')
# green = sourceProduct.getBand('B3')
# blue = sourceProduct.getBand('B2')
# write_rgb_image([red, green, blue], 'snappy_write_image_rgb.png', image_format)
#
# # This cast is need because otherwise jpy can't evaluate which method to call
# # This is considered as an issue of jpy (https://github.com/bcdev/jpy/issues/89)
# rendered_legend_image = jpy.cast(legend_image, RenderedImage)
# JAI.create("filestore", rendered_legend_image, 'snappy_write_image_legend.png', image_format)
#
# red = sourceProduct.getBand('B4')
# green = sourceProduct.getBand('B3')
# blue = sourceProduct.getBand('B2')
# write_rgb_image([red, green, blue], 'snappy_write_image_rgb.png', image_format)


#
# import snappy
# import sys
# from snappy import (ProductIO, ProductUtils, ProgressMonitor)
#
# # if len(sys.argv) != 2:
# #     print("usage: %s <file>" % sys.argv[0])
# #     sys.exit(1)
# #
# # file = sys.argv[1]
#
#
# # import rasterio
# # import numpy as np
# from os import path, listdir
# # from tempfile import mkstemp
# # from osgeo import gdal
# # # import os, rasterio
# import glob
# # import subprocess
#
# basedir = '/home/nils/birdhouse/var/lib/pywps/cache/flyingpigeon/scihub.copernicus/S2A_MSIL1C_20170119T092311_N0204_R093_T33PVK_20170119T093234.SAFE/'
#
# prefix = path.basename(path.normpath(basedir)).split('.')[0]
#
# jps = []
# fname = basedir.split('/')[-1]
# ID = fname.replace('.SAVE','')
#
# for filename in glob.glob(basedir + '/GRANULE/*/IMG_DATA/*jp2'):
#     jps.append(filename)
#
# jp_B04 = [jp for jp in jps if '_B04.jp2' in jp][0]
# jp_B08 = [jp for jp in jps if '_B08.jp2' in jp][0]
#
#
#
# jpy = snappy.jpy
#
# # More Java type definitions required for image generation
# Color = jpy.get_type('java.awt.Color')
# ColorPoint = jpy.get_type('org.esa.snap.core.datamodel.ColorPaletteDef$Point')
# ColorPaletteDef = jpy.get_type('org.esa.snap.core.datamodel.ColorPaletteDef')
# ImageInfo = jpy.get_type('org.esa.snap.core.datamodel.ImageInfo')
# ImageLegend = jpy.get_type('org.esa.snap.core.datamodel.ImageLegend')
# ImageManager = jpy.get_type('org.esa.snap.core.image.ImageManager')
# JAI = jpy.get_type('javax.media.jai.JAI')
# RenderedImage = jpy.get_type('java.awt.image.RenderedImage')
#
#
# # Disable JAI native MediaLib extensions
# System = jpy.get_type('java.lang.System')
# System.setProperty('com.sun.media.jai.disableMediaLib', 'true')
#
# def write_image(band, filename, format):
#     im = ImageManager.getInstance().createColoredBandImage([band], band.getImageInfo(), 0)
#     JAI.create("filestore", im, filename, format)
#
# def write_rgb_image(bands, filename, format):
#     image_info = ProductUtils.createImageInfo(bands, True, ProgressMonitor.NULL)
#     im = ImageManager.getInstance().createColoredBandImage(bands, image_info, 0)
#     JAI.create("filestore", im, filename, format)
#
# product = ProductIO.readProduct(file)
# band = product.getBand('radiance_13')
#
# # The colour palette assigned to pixel values 0, 50, 100 in the band's geophysical units
# points = [ColorPoint(0.0, Color.YELLOW),
#           ColorPoint(50.0, Color.RED),
#           ColorPoint(100.0, Color.BLUE)]
# cpd = ColorPaletteDef(points)
# ii = ImageInfo(cpd)
# band.setImageInfo(ii)
#
# image_format = 'PNG'
# write_image(band, 'snappy_image.png', image_format)
#
# legend = ImageLegend(band.getImageInfo(), band)
# legend.setHeaderText(band.getName())
#
# #legend.setOrientation(ImageLegend.HORIZONTAL) # or ImageLegend.VERTICAL
# #legend.setFont(legend.getFont().deriveFont(14))
# #legend.setBackgroundColor(Color.CYAN)
# #legend.setForegroundColor(Color.ORANGE);
# #legend.setBackgroundTransparency(0.7);
# #legend.setBackgroundTransparencyEnabled(True);
# #legend.setAntialiasing(True);
#
# legend_image = legend.createImage()
#
# # This cast is need because otherwise jpy can't evaluate which method to call
# # This is considered as an issue of jpy (https://github.com/bcdev/jpy/issues/89)
# rendered_legend_image = jpy.cast(legend_image, RenderedImage)
# JAI.create("filestore", rendered_legend_image, 'snappy_write_image_legend.png', image_format)
#
# red = product.getBand('radiance_13')
# green = product.getBand('radiance_5')
# blue = product.getBand('radiance_1')
# write_rgb_image([red, green, blue], 'snappy_write_image_rgb.png', image_format)
