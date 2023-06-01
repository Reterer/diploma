<template>
    <v-network-graph class="graph" :nodes="item.public_data.nodes" :edges="item.public_data.edges" :configs="configs">
        <template #override-node-label="{
            nodeId, scale, text, x, y, config, textAnchor, dominantBaseline
        }">
            <text x="0" y="0" :font-size="9 * scale" text-anchor="middle" dominant-baseline="central" fill="#ffffff">{{
                nodeId }}</text>
            <!-- <text x="0" y="0" :font-size="config.fontSize * scale" :text-anchor="textAnchor"
                :dominant-baseline="dominantBaseline" :fill="config.color" :transform="`translate(${x} ${y})`">{{ text
                }}</text> -->
        </template>
    </v-network-graph>
    <h5>Найдите инварианты заданного графа</h5>
    <div class="answer_block">
        <div class="form-floating mb-3">
            <input v-model="answer.vertex" type="number" class="form-control mb-3" id="vertexInput"
                placeholder="Количество вершин" @change="onChecked">
            <label for="vertexInput">Количество вершин</label>
        </div>
        <div class="form-floating mb-3">
            <input v-model="answer.edges" type="number" class="form-control mb-3" id="edgesInput"
                placeholder="Количество ребер" @change="onChecked">
            <label for="edgesInput">Количество ребер</label>
        </div>
        <div class="form-floating mb-3">
            <input v-model="answer.chromo" type="number" class="form-control mb-3" id="chromoInput"
                placeholder="Хроматическое число" @change="onChecked">
            <label for="chromoInput">Хроматическое число</label>
        </div>
        <div class="form-floating mb-3">
            <input v-model="answer.compo" type="number" class="form-control mb-3" id="chromoInput"
                placeholder="Число компонент связности" @change="onChecked">
            <label for="chromoInput">Число компонент связности</label>
        </div>
    </div>
</template>

<script>
import * as vNG from "v-network-graph"
export default {
    data() {
        return {
            nodes: {
                node1: { name: "Node 1" },
                node2: { name: "Node 2" },
                node3: { name: "Node 3" },
                node4: { name: "Node 4" },
            },
            edges: {
                edge1: { source: "node1", target: "node2" },
                edge2: { source: "node2", target: "node3" },
                edge3: { source: "node3", target: "node4" },
            },
            configs: vNG.defineConfigs({
                view: {
                    scalingObjects: true,
                    minZoomLevel: 1,
                }
            }),
            answer: {
                vertex: '',
                edges: '',
                chromo: '',
                compo: '',
            }
        }
    },
    props: {
        item: Object,
    },
    methods: {
        onChecked(e) {
            console.log("hi")
            this.$emit('answered', this.answer)
        }
    }
}
</script>

<style scoped>
.graph {
    width: 700px;
    height: 400px;
    border: 1px solid #ced4da;
    border-radius: 5px;
}

.answer_block {
    width: 700px;
    height: 400px;
    /* border: 1px solid #000; */
}
</style>