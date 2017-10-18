import graphviz as gv
import pltools.graph as plg


RVector = ("RVector",
           [("a", "void **a"), "len", "capacity"])
RBinHeap = ("RBinHeap", [RVector, ("cmp", "int (*cmp)(const void *a, const void *b)")])


def main():
    d_structs = gv.Digraph(name="cluster_structs")
    d_structs.attr(label="structs")
    d_structs.node_attr["shape"] = "record"

    d_structs.node("v1", label=plg.struct_to_label(RVector))
    d_structs.node("h1", label=plg.struct_to_label(RBinHeap))
    d_structs.node("h2", label=plg.struct_to_label(RBinHeap))

    d_structs.edge("h1:a", "h2:RBinHeap")

    d_funcs = gv.Digraph(name="cluster_funcs")
    d_funcs.attr(label="Function CFG")
    # graph_attr["splines"] = "ortho"

    d_funcs.node(name="R_NEW", label="#define R_NEW(x) (x*)malloc(sizeof(x))")

    d_funcs.edges([["r_binheap_clear", "r_vector_clear"]])
    d_funcs.edges([["r_binheap_init", "r_vector_init"]])
    d_funcs.edges([["r_binheap_new", "R_NEW"]])
    d_funcs.edges([["r_binheap_pop", "_heap_down"]])
    d_funcs.edges([["r_binheap_push", "r_vector_push"], ["r_vector_push", "_heap_up"]])

    plg.nodes(d_funcs, [
        ("R_NEW0", "#define R_NEW0(x) (x*)calloc(1,sizeof(x))"),
        ("RESIZE_OR_RETURN_NULL", '''#define RESIZE_OR_RETURN_NULL(next_capacity) do { \\
        int new_capacity = next_capacity; \\
        void **new_a = realloc (vec->a, sizeof(void *) * new_capacity); \\
        if (!new_a) { \\
            return NULL; \\
        } \\
        vec->a = new_a; \\
        vec->capacity = new_capacity; \\
    } while (0)'''),
        ("NEXT_VECTOR_CAPACITY", """#define NEXT_VECTOR_CAPACITY (vec->capacity < INITIAL_VECTOR_LEN \\
    ? INITIAL_VECTOR_LEN \\
    : vec->capacity <= 12 ? vec->capacity * 2 \\
    : vec->capacity + (vec->capacity >> 1))"""),
        ("R_FREE", "#define R_FREE(x) { free(x); x = NULL; }"),
    ])
    d_funcs.edge("r_vector_clear", "R_FREE")
    plg.arrow(d_funcs, ["r_vector_clone", ["R_NEW", "malloc", "R_FREE", "memcpy"]])

    d_includes = gv.Digraph(name="cluster_includes")
    d_includes.attr(label="Includes")

    plg.arrow(d_includes, ["binheap.c", "r_binheap.h", "r_vector.h", "r_types.h"])
    plg.arrow(d_includes, ["r_types.h", ["r_userconf.h", "<r_endian.h>", "r_util/r_str_util.h", "<sys/param.h>",
                                         "<r_types_base.h>",
                                         "<sys/types.h>", "<sys/stat.h>", "<dirent.h>", "<unistd.h>",
                                         "<sys/time.h>",
                                         "<winsock2.h>", "<windows.h>", "<stdio.h>", "<string.h>", "<stdlib.h>",
                                         "<stdarg.h>", "<fcntl.h>"]])
    plg.arrow(d_includes, ["r_vector.c", "r_vector.h"])

    d = gv.Digraph()
    # d.graph_attr["splines"] = "ortho"
    d.node_attr["shape"] = "box"
    d.subgraph(d_structs)
    d.subgraph(d_funcs)
    d.subgraph(d_includes)
    plg.xdot(d)


if __name__ == '__main__':
    main()
