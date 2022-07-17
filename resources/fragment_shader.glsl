#version 330


uniform float time;


out vec4 frag_color;


vec3 color(vec2 uv) {
    return vec3(
        0.5 + 0.5 * sin(time + uv.x * 10.0),
        0.5 + 0.5 * sin(time + uv.y * 10.0),
        0.5 + 0.5 * sin(time + uv.x * 10.0 + uv.y * 10.0)
    );
}


void main() {
    frag_color = vec4(color(gl_FragCoord.xy), 1.0);
}