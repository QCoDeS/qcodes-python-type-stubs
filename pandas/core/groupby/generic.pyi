from matplotlib.axes import Axes as PlotAxes, SubplotBase as AxesSubplot
import numpy as np
import sys
from pandas._typing import FrameOrSeries as FrameOrSeries, AxisType, Dtype, Level, F
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.groupby.groupby import GroupBy as GroupBy #, get_groupby as get_groupby
from pandas.core.groupby.grouper import Grouper as Grouper
from pandas.core.series import Series as Series
from typing import Any, Callable, Dict, FrozenSet, NamedTuple, Optional, Sequence, Tuple, Type, Union, overload
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

class NamedAgg(NamedTuple):
    column = ...
    aggfunc = ...

AggScalar = Union[str, Callable[..., Any]]
ScalarResult = ...

def generate_property(name: str, klass: Type[FrameOrSeries]) : ...
def pin_whitelisted_properties(klass: Type[FrameOrSeries], whitelist: FrozenSet[str]) : ...

class SeriesGroupBy(GroupBy):
    def apply(self, func, *args, **kwargs): ...
    def aggregate(self, func = ..., *args, **kwargs) -> Series: ...
    agg = aggregate
    def transform(self, func, *args, **kwargs): ...
    def filter(self, func, dropna: bool = ..., *args, **kwargs): ...
    def nunique(self, dropna: bool = ...) -> Series: ...
    def describe(self, **kwargs) -> Series[np.double64]: ...
    def value_counts(
        self, normalize: bool = ..., sort: bool = ..., ascending: bool = ..., bins = ..., dropna: bool = ...,
    ) -> DataFrame: ...
    def count(self) -> Series[Dtype]: ...
    def pct_change(
        self, periods: int = ..., fill_method: str = ..., limit = ..., freq = ..., axis: AxisType = ...,
    ) -> Series[Dtype]: ...
    # Overrides and others from original pylance stubs
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def __getitem__(self, item: str) -> Series[Dtype]: ...
    def bfill(self, limit: Optional[int] = ...) -> Series[Dtype]: ...
    def cummax(self, axis: AxisType = ..., **kwargs) -> Series[Dtype]: ...
    def cummin(self, axis: AxisType = ..., **kwargs) -> Series[Dtype]: ...
    def cumprod(self, axis: AxisType = ..., **kwargs) -> Series[Dtype]: ...
    def cumsum(self, axis: AxisType = ..., **kwargs) -> Series[Dtype]: ...
    def ffill(self, limit: Optional[int] = ...) -> Series[Dtype]: ...
    def first(self, **kwargs) -> Series[Dtype]: ...
    def head(self, n: int = ...) -> Series[Dtype]: ...
    def last(self, **kwargs) -> Series[Dtype]: ...
    def max(self, **kwargs) -> Series[Dtype]: ...
    def mean(self, **kwargs) -> Series[Dtype]: ...
    def median(self, **kwargs) -> Series[Dtype]: ...
    def min(self, **kwargs) -> Series[Dtype]: ...
    def nlargest(self, n: int = ..., keep: str = ...) -> Series[Dtype]: ...
    def nsmallest(self, n: int = ..., keep: str = ...) -> Series[Dtype]: ...
    def nth(self, n: Union[int, Sequence[int]], dropna: Optional[str] = ...) -> Series[Dtype]: ...


class DataFrameGroupBy(GroupBy):
    @overload
    def aggregate(self, arg: str, *args, **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, arg: Dict, *args, **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, arg: Callable[[], Any], *args, **kwargs) -> DataFrame: ...
    @overload
    def agg(self, arg: str, *args, **kwargs) -> DataFrame: ...
    @overload
    def agg(self, arg: Dict, *args, **kwargs) -> DataFrame: ...
    @overload
    def agg(self, arg: F, *args, **kwargs) -> DataFrame: ...
    def transform(self, func, *args, **kwargs): ...
    def filter(self, func: Callable, dropna: bool = ..., *args, **kwargs) -> DataFrame: ...
    @overload
    def __getitem__(self, item: str) -> SeriesGroupBy: ...
    @overload
    def __getitem__(self, item: Sequence[str]) -> DataFrameGroupBy: ...
    def count(self) -> DataFrame: ...
    def nunique(self, dropna: bool = ...) -> DataFrame: ...
    def boxplot(
        self,
        grouped: DataFrame,
        subplots: bool = ...,
        column: Optional[Union[str, Sequence]] = ...,
        fontsize: Union[int, str] = ...,
        rot: float = ...,
        grid: bool = ...,
        ax: Optional[PlotAxes] = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        sharex: bool = ...,
        sharey: bool = ...,
        bins: Union[int, Sequence] = ...,
        backend: Optional[str] = ...,
        **kwargs
    ) -> Union[AxesSubplot, Sequence[AxesSubplot]]: ...
    # Overrides and others from original pylance stubs
    ## These are "properties" but properties can't have all these arguments?!
    def corr(self, method: Union[str, Callable], min_periods: int = ...) -> DataFrame: ...
    def cov(self, min_periods: int = ...) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: AxisType = ...) -> DataFrame: ...


    def bfill(self, limit: Optional[int] = ...) -> DataFrame: ...

    def corrwith(self, other: DataFrame, axis: AxisType = ..., drop: bool = ..., method: str = ...,) -> Series: ...

    def cummax(self, axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def cummin(self, axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def cumprod(self, axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def cumsum(self, axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def describe(self, **kwargs) -> DataFrame: ...
    def ffill(self, limit: Optional[int] = ...) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value,
        method: Optional[str] = ...,
        axis: AxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def fillna(
        self,
        value,
        method: Optional[str] = ...,
        axis: AxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[False]
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value,
        method: Optional[str] = ...,
        axis: AxisType = ...,
        inplace: bool = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> Union[None, DataFrame]: ...

    def first(self, **kwargs) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def hist(
        self,
        data: DataFrame,
        column: Optional[Union[str, Sequence]] = ...,
        by = ...,
        grid: bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        ax: Optional[PlotAxes] = ...,
        sharex: bool = ...,
        sharey: bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        bins: Union[int, Sequence] = ...,
        backend: Optional[str] = ...,
        **kwargs
    ) -> Union[AxesSubplot, Sequence[AxesSubplot]]: ...
    def idxmax(self, axis: AxisType = ..., skipna: bool = ...) -> Series: ...
    def idxmin(self, axis: AxisType = ..., skipna: bool = ...) -> Series: ...
    def last(self, **kwargs) -> DataFrame: ...
    @overload
    def mad(
        self,
        axis: AxisType = ...,
        skipna: bool = ...,
        numeric_only: Optional[bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def mad(
        self,
        axis: AxisType = ...,
        skipna: bool = ...,
        level: None = ...,
        numeric_only: Optional[bool] = ...,
        **kwargs
    ) -> Series: ...
    def max(self, **kwargs) -> DataFrame: ...
    def mean(self, **kwargs) -> DataFrame: ...
    def median(self, **kwargs) -> DataFrame: ...
    def min(self, **kwargs) -> DataFrame: ...
    def nth(self, n: Union[int, Sequence[int]], dropna: Optional[str] = ...) -> DataFrame: ...

    def pct_change(
        self, periods: int = ..., fill_method: str = ..., limit = ..., freq = ..., axis: AxisType = ...,
    ) -> DataFrame: ...
    def prod(self, **kwargs) -> DataFrame: ...
    def quantile(self, q: float = ..., interpolation: str = ...) -> DataFrame: ...
    def rank(
        self, method: str = ..., ascending: bool = ..., na_option: str = ..., pct: bool = ..., axis: AxisType = ...,
    ) -> DataFrame: ...
    def resample(self, rule, *args, **kwargs) -> Grouper: ...
    def sem(self, ddof: int = ...) -> DataFrame: ...
    def shift(
        self, periods: int = ..., freq: str = ..., axis: AxisType = ..., fill_value = ...,
    ) -> DataFrame: ...
    def size(self) -> Series[int]: ...
    @overload
    def skew(
        self, axis: AxisType = ..., skipna: bool = ..., numeric_only: bool = ..., *, level: Level, **kwargs
    ) -> DataFrame: ...
    @overload
    def skew(
        self, axis: AxisType = ..., skipna: bool = ..., level: None = ..., numeric_only: bool = ..., **kwargs
    ) -> Series: ...
    def std(self, ddof: int = ...) -> DataFrame: ...
    def sum(self, **kwargs) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def take(self, indices: Sequence, axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def tshift(self, periods: int, freq = ..., axis: AxisType = ...) -> DataFrame: ...
    def var(self, ddof: int = ...) -> DataFrame: ...

