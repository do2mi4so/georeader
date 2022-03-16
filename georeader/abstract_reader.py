import numpy as np
from georeader.geotensor import GeoTensor
from typing import Tuple,Any, Union
import rasterio
import rasterio.windows


class AbstractGeoData:
    def __init__(self):
        self.dtype = np.float32
        self.dims = ("y", "x")
        # TODO replace fill_value_default with nodata
        self.fill_value_default = 0

    @property
    def shape(self) -> Tuple:
        # return 1000, 3000
        raise NotImplementedError("Not implemented")

    @property
    def transform(self) -> rasterio.Affine:
        # return rasterio.Affine(10, 0, 200, 0, 10, 400)
        raise NotImplementedError("Not implemented")

    @property
    def res(self) -> Tuple[float, float]:
        transform = self.transform
        #  compute resolution for non-rectilinear transforms!
        z0_0 = np.array(transform * (0, 0))
        z0_1 = np.array(transform * (0, 1))
        z1_0 = np.array(transform * (1, 0))

        return np.sqrt(np.sum((z0_0-z1_0)**2)), np.sqrt(np.sum((z0_0-z0_1)**2))

    @property
    def crs(self) -> Any:
        # return "EPSG:4326"
        raise NotImplementedError("Not implemented")

    @property
    def bounds(self) -> Tuple[float, float, float, float]:
        return rasterio.windows.bounds(rasterio.windows.Window(col_off=0, row_off=0, width=self.shape[-1], height=self.shape[-2]),
                                       self.transform)

    def read_from_window(self, window:rasterio.windows.Window, boundless:bool) -> Union['__class__', GeoTensor]:
        # return GeoTensor(values=self.values, transform=self.transform, crs=self.crs)
        raise NotImplementedError("Not implemented")

    def load(self, boundless:bool=True)-> GeoTensor:
        # return GeoTensor(values=self.values, transform=self.transform, crs=self.crs)
        raise NotImplementedError("Not implemented")

    @property
    def values(self) -> np.ndarray:
        # return np.zeros(self.shape, dtype=self.dtype)
        raise NotImplementedError("Not implemented")
