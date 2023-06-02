<template>
    <v-network-graph class="graph" :nodes="nodes" :edges="edges" :configs="configs">
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
                1: { name: "1" },
                2: { name: "2" },
                3: { name: "3" },
                4: { name: "4" },
                5: { name: "5" },
                6: { name: "6" },
                7: { name: "7" },
                8: { name: "8" },
            },
            edges: {
                1: { source: 1, target: 2 },
                4: { source: 1, target: 3 },
                2: { source: 2, target: 3 },
                3: { source: 2, target: 4 },
                5: { source: 2, target: 5 },
                6: { source: 3, target: 4 },
                7: { source: 6, target: 7 },
                8: { source: 7, target: 8 },
                9: { source: 8, target: 6 },
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