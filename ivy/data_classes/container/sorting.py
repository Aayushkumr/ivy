# global
from typing import Optional, List, Union, Dict, Literal

# local
from ivy.data_classes.container.base import ContainerBase
import ivy

# ToDo: implement all methods here as public instance methods


# noinspection PyMissingConstructor
class _ContainerWithSorting(ContainerBase):
    @staticmethod
    def _static_argsort(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.argsort. This method simply wraps the
        function, and so the docstring for ivy.argsort also applies to this method with
        minimal changes.

        Parameters
        ----------
        x
            input array or container. Should have a numeric data type.
        axis
            axis along which to sort. If set to ``-1``, the function must sort
            along the last axis. Default: ``-1``.
        descending
            sort order. If ``True``, the returned indices sort
            ``x`` in descending order (by value). If ``False``,
            the returned indices sort ``x`` in ascending order
            (by value). Default: ``False``.
        stable
            sort stability. If ``True``, the returned indices must maintain
            the relative order of ``x`` values which compare as equal.
            If ``False``, the returned indices may or may not maintain
            the relative order of ``x`` values which compare as equal (i.e., the
            relative order of ``x`` values which compare as equal
            is implementation-dependent). Default: ``True``.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            a container containing the index values of sorted
            array. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        With :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([7, 2, 1]),
        ...                   b=ivy.array([3, 2]))
        >>> y = ivy.Container.static_argsort(x, axis=-1, descending=True, stable=False)
        >>> print(y)
        {
            a: ivy.array([0, 1, 2]),
            b: ivy.array([0, 1])
        }

        >>> x = ivy.Container(a=ivy.array([7, 2, 1]),
        ...                   b=ivy.array([[3, 2], [7, 0.2]]))
        >>> y = ivy.Container.static_argsort(x, axis=-1, descending=True, stable=False)
        >>> print(y)
        {
            a: ivy.array([0, 1, 2]),
            b: ivy.array([[0, 1]],[0, 1]])
        }

        With :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([2, 5, 1]),
        ...                   b=ivy.array([1, 5], [.2,.1]))
        >>> y = ivy.Container.static_argsort(x,axis=-1, descending=True, stable=False)
        >>> print(y)
        {
            a: ivy.array([2, 0, 1]),
            b: ivy.array([[1, 0],[0,1]])
        }

        >>> x = ivy.Container(a=ivy.native_array([2, 5, 1]),
        ...                   b=ivy.array([1, 5], [.2,.1]))
        >>> y = ivy.Container.static_argsort(x, axis=-1, descending=True, stable=False)
        >>> print(y)
        {
            a: ivy.array([2, 0, 1]),
            b: ivy.array([[1, 0],[0,1]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "argsort",
            x,
            axis=axis,
            descending=descending,
            stable=stable,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def argsort(
        self: ivy.Container,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.argsort. This method simply wraps
        the function, and so the docstring for ivy.argsort also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            input array or container. Should have a numeric data type.
        axis
            axis along which to sort. If set to ``-1``, the function
            must sort along the last axis. Default: ``-1``.
        descending
            sort order. If ``True``, the returned indices sort ``x``
            in descending order (by value). If ``False``, the
            returned indices sort ``x`` in ascending order (by value).
            Default: ``False``.
        stable
            sort stability. If ``True``, the returned indices must
            maintain the relative order of ``x`` values which compare
            as equal. If ``False``, the returned indices may or may not
            maintain the relative order of ``x`` values which compare
            as equal (i.e., the relative order of ``x`` values which
            compare as equal is implementation-dependent).
            Default: ``True``.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains,
            otherwise key_chains will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to.
            It must have a shape that the inputs broadcast to.

        Returns
        -------
        ret
            a container containing the index values of sorted array.
            The returned array must have a data type determined
            by :ref:`type-promotion`.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([7, 2, 1]),
        ...                   b=ivy.array([3, 2]))
        >>> y = x.argsort(axis=-1, descending=True, stable=False)
        >>> print(y)
        {
            a: ivy.array([0, 1, 2]),
            b: ivy.array([0, 1])
        }
        """
        return self._static_argsort(
            self,
            axis=axis,
            descending=descending,
            stable=stable,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def _static_sort(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.sort. This method simply wraps the
        function, and so the docstring for ivy.sort also applies to this method with
        minimal changes.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([5, 9, 0.2]),
        ...                   b=ivy.array([[8, 1], [5, 0.8]]))
        >>> y = ivy.Container.static_sort(x)
        >>> print(y)
        {
            a: ivy.array([0.2, 5., 9.]),
            b: ivy.array([[1., 8.], [0.8, 5.]])
        }

        >>> x = ivy.Container(a=ivy.array([8, 0.5, 6]),
        ...                   b=ivy.array([[9, 0.7], [0.4, 0]]))
        >>> y = ivy.Container.static_sort(x)
        >>> print(y)
        {
            a: ivy.array([0.5, 6., 8.]),
            b: ivy.array([[0.7, 9.], [0., 0.4]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "sort",
            x,
            axis=axis,
            descending=descending,
            stable=stable,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def sort(
        self: ivy.Container,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.sort. This method simply wraps the
        function, and so the docstring for ivy.sort also applies to this method with
        minimal changes.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([5, 9, 0.2]),
        ...                   b=ivy.array([8, 1]))
        >>> y = x.sort()
        >>> print(y)
        {
            a: ivy.array([0.2, 5., 9.]),
            b: ivy.array([1, 8])
        }

        >>> x = ivy.Container(a=ivy.array([5, 9, 0.2]),
        ...                   b=ivy.array([[8, 1], [5, 0.8]]))
        >>> y = x.sort()
        >>> print(y)
        {
            a: ivy.array([0.2, 5., 9.]),
            b: ivy.array([[1., 8.], [0.8, 5.]])
        }

        >>> x = ivy.Container(a=ivy.array([8, 0.5, 6]),
        ...                   b=ivy.array([[9, 0.7], [0.4, 0]]))
        >>> y = ivy.sort(x)
        >>> print(y)
        {
            a: ivy.array([0.5, 6., 8.]),
            b: ivy.array([[0.7, 9.],[0., 0.4]])
        }

        >>> x = ivy.Container(a=ivy.native_array([8, 0.5, 6]),
        ...                   b=ivy.array([[9, 0.7], [0.4, 0]]))
        >>> y = ivy.sort(x)
        >>> print(y)
        {
            a: ivy.array([0.5, 6., 8.]),
            b: ivy.array([[0.7, 9.],[0., 0.4]])
        }
        """
        return self._static_sort(
            self,
            axis=axis,
            descending=descending,
            stable=stable,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_msort(
        a: Union[ivy.Array, ivy.NativeArray, ivy.Container, list, tuple],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.msort. This method simply wraps the
        function, and so the docstring for ivy.msort also applies to this method with
        minimal changes.

        Parameters
        ----------
        a
            array-like or container input.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            a container containing sorted input arrays.

        Examples
        --------
        With :class:`ivy.Container` input:

        >>> a = ivy.Container(x = ivy.asarray([[8, 9, 6],[6, 2, 6]]),
        ...                   y = ivy.asarray([[7, 2],[3, 4]])
        >>> ivy.Container.static_lexsort(a)
        {
            x: ivy.array(
                [[6, 2, 6],
                 [8, 9, 6]]
                ),
            y: ivy.array(
                [[3, 4],
                 [7, 2]]
                )
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "msort",
            a,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def msort(
        self: ivy.Container,
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.msort. This method simply wraps the
        function, and so the docstring for ivy.msort also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            input container with array-like inputs to sort.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            a container containing the sorted input arrays.

        Examples
        --------
        >>> a = ivy.Container(x = ivy.asarray([[8, 9, 6],[6, 2, 6]]),
        ...                   y = ivy.asarray([[7, 2],[3, 4]])
        >>> a.msort()
        {
            x: ivy.array(
                [[6, 2, 6],
                 [8, 9, 6]]
                ),
            y: ivy.array(
                [[3, 4],
                 [7, 2]]
                )
        }
        """
        return self.static_msort(
            self,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )


@staticmethod
def _static_argpartition(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kth: Union[int, ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    axis: int = -1,
    kind: str = "introselect",
    order: Optional[Union[str, List[str]]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of numpy.argpartition.

    Perform an indirect partition along the given axis using the algorithm specified by the kind keyword.
    It returns an array of indices of the same shape as `x` that index data along the given axis in partitioned order.

    Parameters
    ----------
    x : Union[ivy.Array, ivy.NativeArray, ivy.Container]
        Input array or container.
    kth : Union[int, ivy.Array, ivy.NativeArray, ivy.Container]
        Element index to partition by.
    axis : int, optional
        Axis along which to sort. If not provided, the last axis is used. Default is -1.
    kind : str, optional
        Algorithm used to select the partition. Default is 'introselect'.
    order : Optional[Union[str, List[str]]], optional
        If `x` is a structured array or a container of structured arrays, this parameter specifies the field(s) to use for sorting.
        Default is None.
    key_chains : Optional[Union[List[str], Dict[str, str]]], optional
        The key-chains to apply or not apply the method to. Default is None.
    to_apply : bool, optional
        If True, the method will be applied to key_chains, otherwise key_chains will be skipped. Default is True.
    prune_unapplied : bool, optional
        Whether to prune key_chains for which the function was not applied. Default is False.
    map_sequences : bool, optional
        Whether to also map the method to sequences (lists, tuples). Default is False.
    out : Optional[ivy.Container], optional
        Optional output container, for writing the result to. It must have a shape that the inputs broadcast to.

    Returns
    -------
    ivy.Container
        A container containing the indices of `x` that index data along the given axis in partitioned order.

    Examples
    --------
    With ivy.Container input:

    >>> x = ivy.Container(a=ivy.array([3, 4, 2, 1]),
    ...                   b=ivy.array([[9, 5], [7, 8], [2, 4], [1, 6]]))
    >>> kth = ivy.Container(a=2, b=1)
    >>> y = ivy.Container._static_argpartition(x, kth, axis=-1)
    >>> print(y)
    {
        a: ivy.array([3, 2, 1, 0]),
        b: ivy.array([[4, 3], [2, 0], [0, 2], [1, 1]])
    }
    """
    return ContainerBase.cont_multi_map_in_function(
        "argpartition",
        x,
        kth,
        axis=axis,
        kind=kind,
        order=order,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
        out=out,
    )


def argpartition(
    self: ivy.Container,
    kth: Union[int, ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    axis: int = -1,
    kind: str = "introselect",
    order: Optional[Union[str, List[str]]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of numpy.argpartition.

    Perform an indirect partition along the given axis using the algorithm specified by the kind keyword.
    It returns an array of indices of the same shape as `self` that index data along the given axis in partitioned order.

    Parameters
    ----------
    self : ivy.Container
        Input array or container.
    kth : Union[int, ivy.Array, ivy.NativeArray, ivy.Container]
        Element index to partition by.
    axis : int, optional
        Axis along which to sort. If not provided, the last axis is used. Default is -1.
    kind : str, optional
        Algorithm used to select the partition. Default is 'introselect'.
    order : Optional[Union[str, List[str]]], optional
        If `self` is a structured array or a container of structured arrays, this parameter specifies the field(s) to use for sorting.
        Default is None.
    key_chains : Optional[Union[List[str], Dict[str, str]]], optional
        The key-chains to apply or not apply the method to. Default is None.
    to_apply : bool, optional
        If True, the method will be applied to key_chains, otherwise key_chains will be skipped. Default is True.
    prune_unapplied : bool, optional
        Whether to prune key_chains for which the function was not applied. Default is False.
    map_sequences : bool, optional
        Whether to also map the method to sequences (lists, tuples). Default is False.
    out : Optional[ivy.Container], optional
        Optional output container, for writing the result to. It must have a shape that the inputs broadcast to.

    Returns
    -------
    ivy.Container
        A container containing the indices of `self` that index data along the given axis in partitioned order.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([3, 4, 2, 1]),
    ...                   b=ivy.array([[9, 5], [7, 8], [2, 4], [1, 6]]))
    >>> kth = ivy.Container(a=2, b=1)
    >>> y = x.argpartition(kth, axis=-1)
    >>> print(y)
    {
        a: ivy.array([3, 2, 1, 0]),
        b: ivy.array([[4, 3], [2, 0], [0, 2], [1, 1]])
    }
    """
    return self._static_argpartition(
        self,
        kth,
        axis=axis,
        kind=kind,
        order=order,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
        out=out,
    )

    @staticmethod
    def _static_searchsorted(
        x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        v: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        side="left",
        sorter: Optional[
            Union[ivy.Array, ivy.NativeArray, ivy.Container, List[int]]
        ] = None,
        ret_dtype=ivy.int64,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.searchsorted.

        This method simply wraps the function, and so the docstring for
        ivy.searchsorted also applies to this method with minimal
        changes.
        """
        return ContainerBase.cont_multi_map_in_function(
            "searchsorted",
            x1,
            v,
            side=side,
            sorter=sorter,
            ret_dtype=ret_dtype,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def searchsorted(
        self: ivy.Container,
        v: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        side: Literal["left", "right"] = "left",
        sorter: Optional[Union[ivy.Array, ivy.NativeArray, List[int]]] = None,
        ret_dtype: Union[ivy.Dtype, ivy.NativeDtype] = ivy.int64,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.searchsorted.

        This method simply wraps the function, and so the docstring for
        ivy.searchsorted also applies to this method with minimal
        changes.
        """
        return self._static_searchsorted(
            self,
            v,
            side=side,
            sorter=sorter,
            ret_dtype=ret_dtype,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )
