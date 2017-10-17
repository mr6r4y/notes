import graphviz as gv
import pltools.graph as plg


RVector = ("RVector",
           [("a", "void **a"), "len", "capacity"])
RBinHeap = ("RBinHeap", [RVector, ("cmp", "int (*cmp)(const void *a, const void *b)")])


def main():
    d_structs = gv.Digraph(name="cluster_structs")
    d_structs.attr(label="structs")
    d_structs.node_attr["shape"] = "record"
    # d_structs.graph_attr["splines"] = "ortho"
    # d_structs.attr(rankdir="LR")

    d_structs.node("h1", label=plg.struct_to_label(RBinHeap))
    d_structs.node("h2", label=plg.struct_to_label(RBinHeap))

    d_structs.edge("h1:a", "h2:RBinHeap")

    d_funcs = gv.Digraph(name="cluster_funcs")
    d_funcs.attr(label="Function CFG")

    d_funcs.edges([["r_binheap_clear", "r_vector_clear"]])
    d_funcs.edges([["r_binheap_init", "r_vector_init"]])
    d_funcs.edges([["r_binheap_new", "R_NEW"], ["R_NEW", "malloc(sizeof(..))"]])
    d_funcs.edges([["r_binheap_pop", "_heap_down"]])
    d_funcs.edges([["r_binheap_push", "r_vector_push"], ["r_vector_push", "_heap_up"]])

    d_includes = gv.Digraph(name="cluster_includes")
    d_includes.attr(label="Includes")

    plg.arrow(d_includes, ["binheap.c", "r_binheap.h", "r_vector.h", "r_types.h"])
    plg.arrow(d_includes, ["r_types.h", ["r_userconf.h", "<r_endian.h>", "r_util/r_str_util.h", "<sys/param.h>",
                                         "<winsock2.h>", "<windows.h>", "<stdio.h>", "<string.h>", "<stdlib.h>",
                                         "<stdarg.h>", "<fcntl.h>"]])

    d = gv.Digraph()
    d.subgraph(d_structs)
    d.subgraph(d_funcs)
    d.subgraph(d_includes)
    plg.xdot(d)


if __name__ == '__main__':
    main()
